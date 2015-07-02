#YACLWiN
YACLWiN (Yet Another Configuration Language Without a Name) is a tool to make TAS movies used by [Source Pause Tool](http://wiki.sourceruns.org/wiki/Source_Pause_Tool)

##Requirements
* [Python 3.3+](https://www.python.org/downloads/)
* [Grako 3.6.1+](https://pypi.python.org/pypi/grako/3.6.1)

##Usage
```sh
python converter.py  input.cfg -o output.cfg
```
### Interactive mode
The interactive mode automatically converts the input file to the output file when a new change in the input file is detected.
The interactive mode can be invoked with the following command :
```sh
python converter.py input.cfg -o output.cfg -i
```
You can specify the dependancies of the input file, if one of the dependencies is changed then the output file will be regenerated.
```sh
python converter.py input.cfg -o output.cfg -i -d"dep1.cfg,dep2.cfg"
```

##License
[GPL](http://www.gnu.org/licenses/gpl.txt)

##Commands
###attack
```
attack [duration]
```
Activates the main attack (blue portal) during _duration_ frames. If _duration_ is not set then the attack is activated during 1 frame

###attack2
```
attack2 [duration]
```
Activates the second attack (orange portal) during _duration_ frames. If _duration_ is not set then the attack2 is activated during 1 frame

###back
```
back [duration]
```
Moves backward during _duration_ frames. If _duration_ is not set then movement is activated during 1 frame

###forward
```
forward [duration]
```
Moves forward during _duration_ frames. If _duration_ is not set then movement is activated during 1 frame

###jump
```
jump [duration]
```
Activates the jump during _duration_ frames. If _duration_ is not set then the jump is activated during 1 frame

###left
```
left [duration]
```
Moves to the left during _duration_ frames. If _duration_ is not set then movement is activated during 1 frame

###next
```
next
```
Increaments the frame counter by 1. See wait to increament the frame count by a specified number

###pause
```
pause [frame]
```
Pauses the game at the current frame. If the parameter _frame_ is set then the game is paused at that frame

###resetall
```
resetall
```
Disables attack, attack2, back, forward, left, right, jump, use. Set the (camera) angles to 0.0

###right
```
right [duration]
```
Moves to the right during _duration_ amout of frames. If _duration_ is not set then movement is activated during 1 frame

###setang
```
left x_ang y_ang
```
Sets the orientation of the camera.

###unpause
```
unpause [frame]
```
Unpauses the game at the current frame. If the parameter _frame_ is set then the game is unpaused at that frame

###use
```
use [duration]
```
Activates _use_ during _duration_ frames. If _duration_ is not set then _use_ is activated during 1 frame

###wait
```
wait duration
```
Increments the frame counter by _duration_.
