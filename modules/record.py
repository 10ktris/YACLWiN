def resolve(args, frame):
	if len(args) == 2:
		duration = args[0]
		name = args[1]
		if type(duration) not in (int, float):
			raise TypeError("Wrong type argument : duration")

	else:
		raise Exception("Wrong number of arguments")
	
	result  = '_y_spt_afterframes {} "record" + name \n'.format(frame)
	result += '_y_spt_afterframes {} "stop"'.format(frame + duration)
	return result, frame