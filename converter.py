# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from grako.parsing import graken, Parser
from grammar import *
from multiprocessing import Process
from multiprocessing import Value
from importlib import machinery
import os
import sys
import time
import json

TIME_BETWEEN_CHECKS = 0.5 # in second

def load_modules(dir=None):
    if dir is None:
        dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "modules")
    modules = {}
    for f in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, f)) and f.endswith(".py"):
            module_name = f[:-3]
            try:
                module = machinery.SourceFileLoader(module_name, os.path.join(dir, f))
                module = module.load_module()
            except ImportError as e:
                print("Can't load module", module_name, ":\n", e)
            else:
                modules[module_name] = module
    return modules

def convert_args(args):
    new_args = []
    if not args:
        return new_args
    for arg in args:
        if "int" in arg:
            result = int(arg["int"])
        elif "float" in arg:
            result = float(arg["float"])
        elif "string" in arg:
            result = arg["string"][1:-1] # remove " at begining and end
        new_args.append(result)
    return new_args

def eval_ast(ast, modules, start_frame):
    current_frame = start_frame
    result = ""
    for subast in ast:
        if not subast: continue
        for subsub in subast:
            if "comment" in subsub:
                continue
            if "action" in subsub:
                if "cmd" in subsub["action"]:
                    module_name = subsub["action"]["cmd"]
                    args = convert_args(subsub["action"]["args"])
                    module = modules.get(module_name, None)
                    if not module:
                        raise Exception(("Can't find the module "
                            "corresponding to the function {}'").format(module_name))
                    try:
                        txt, current_frame = module.resolve(args, current_frame)
                    except Exception as e:
                        raise Exception("Error at :\n{} {}\n{}"
                            .format(module_name, " ".join(map(repr, args)), e))
                elif "import" in subsub["action"]:
                    try:
                        txt, current_frame = convert(subsub["action"]["import_"], current_frame)
                    except Exception as e:
                        raise Exception("Error while importing {}.\n{}"
                            .format(subsub["action"]["import_"], e))
                result += "\n" + txt
    return result, current_frame

def parse(filename):
    startrule = "root"

    with open(filename) as f:
        text = f.read()
    parser = grammarParser(parseinfo=False)
    ast = parser.parse(
        text,
        startrule,
        filename=filename,
        trace=False,
        whitespace="",
        nameguard=True)
    return ast

def convert(filename, start_frame=0, root=False):
    ast = parse(filename)
    modules = load_modules()
    txt, frames = eval_ast(ast, modules, start_frame)
    if root:
        # reset the frame count to make the movie sync
        txt = "_y_spt_afterframes_reset\n" + txt
    return txt, frames

def check_new_update(filename, dep, output):
    if not os.path.exists(output):
        return True
    f_mod_time = os.path.getmtime(filename)
    out_mod_time = os.path.getmtime(output)
    if f_mod_time > out_mod_time:
        return True
    for f_dep in dep:
        if os.path.getmtime(f_dep) > out_mod_time:
            return True
    return False

def interactive(filename, dep, output, end):
    last_check = 0
    while not end.value:
        time.sleep(TIME_BETWEEN_CHECKS)
        need_convert = check_new_update(filename, dep, output)
        if need_convert:
            txt = ""
            try:
                txt, current_frame = convert(filename, root=True)
            except Exception as e:
                if last_check <= os.path.getmtime(filename):
                    print("[{}] convertion of {} failed.\n{}".format(time.ctime(time.time()), filename, e))
                    last_check = time.time()
                continue
            with open(output, "w") as f:
                f.write(txt)
            print("[{}] {} converted".format(time.ctime(time.time()), filename))

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Convert files to Source Pause Tool movies")
    parser.add_argument('-i', '--interactive', action='store_true',
                        help='interactive mode')
    parser.add_argument('-o', '--output', type=str, default="",
                        help="the output file")
    parser.add_argument('file', metavar="FILE", help="the input file to convert")
    parser.add_argument('-d', '--dependencies', type=str, default="",
                        help="the dependencies of the file to convert")
    args = parser.parse_args()

    if args.interactive:
        if not args.output:
            print("The ouput file is not optional when the interactive mode is activated")
            exit()
        dep = [f for f in args.dependencies.split(",") if f]
        print("Interactive mode activated "
              "(Press [enter] to quit).\n"
              "Waiting for modifications...")
        end_inter_mode = Value("i", False)
        p = Process(target=interactive, args=(args.file, dep, args.output, end_inter_mode))
        try:
            p.start()
            input("")
        finally:
            end_inter_mode.value = True
            p.join()
    else:
        txt, frames = convert(args.file, root=True)
        if args.output:
            with open(args.output, "w") as f:
                f.write(txt)
        else:
            print(txt)