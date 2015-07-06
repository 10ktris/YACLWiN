def resolve(args, frame):
	if not args:
		duration = 1000
		name = 'TAS_demo'
	elif len(args) == 1:
		duration = args[0]
		name = "TAS_demo"
		if type(duration) != int:
			raise TypeError("Wrong type argument")
	elif len(args) == 2:
		duration = args[0]
		name = args[1]
		if type(duration) != int or type(name) != str:
			raise TypeError("Wrong type argument")
	else:
		raise Exception("Wrong number of arguments")
	
	result  = '_y_spt_afterframes {} "record {}"\n'.format(frame, name)
	result += '_y_spt_afterframes {} "stop"'.format(frame + duration)
	return result, frame