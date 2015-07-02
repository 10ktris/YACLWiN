def resolve(args, frame):
	if not args:
		duration = 0
	elif len(args) == 1:
		duration = args[0]
		if type(duration) != int:
			raise TypeError("Wrong type argument")
	else:
		raise Exception("Wrong number of arguments")
	
	result  = '_y_spt_afterframes {} "+back"\n'.format(frame)
	result += '_y_spt_afterframes {} "-back"'.format(frame + duration)
	return result, frame