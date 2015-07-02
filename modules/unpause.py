def resolve(args, frame):
	if not args:
		pause_at = 0
	elif len(args) == 1:
		pause_at = args[0]
		if type(pause_at) != int:
			raise TypeError("Wrong type argument")
	else:
		raise Exception("Wrong number of arguments")
	
	result  = '_y_spt_afterframes {} "unpause"'.format(pause_at)
	return result, frame