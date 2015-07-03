
def resolve(args, frame, name):
	if not args:
		duration = 1000
		name = 'TAS_demo'
	elif len(args) == 1:
		duration = args[0]
		if type(duration) != int:
			raise TypeError("Wrong type argument")
	else:
		raise Exception("Wrong number of arguments")
	
	result  = '_y_spt_afterframes {} "record '+ name + '"'.\n'.format(frame)
	result += '_y_spt_afterframes {} "stop"'.format(frame + duration)
	return result, frame, name
