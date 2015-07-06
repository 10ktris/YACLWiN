def resolve(args, frame):
	if len(args) == 1:
		angle = args[0]
		if type(angle) not in (int, float):
			raise TypeError("Wrong type argument : angle")
	else:
		raise Exception("Wrong number of arguments")
	result = '_y_spt_afterframes {} "_y_spt_setyaw {}"'.format(frame, angle)
	return result, frame