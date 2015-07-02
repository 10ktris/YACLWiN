def resolve(args, frame):
	if not args:
		duration = 1
	elif len(args) == 1:
		duration = args[0]
		if type(duration) != int:
			raise TypeError("Wrong type argument")
	else:
		raise Exception("Wrong number of arguments")
	
	result  = '_y_spt_afterframes {} "+attack2"\n'.format(frame)
	result += '_y_spt_afterframes {} "-attack2"'.format(frame + duration)
	return result, frame