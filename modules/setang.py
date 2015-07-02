def resolve(args, frame):
	if len(args) == 2:
		x_ang = args[0]
		y_ang = args[1]
		if type(x_ang) not in (int, float):
			raise TypeError("Wrong type argument : x_ang")
		if type(x_ang) not in (int, float):
			raise TypeError("Wrong type argument : y_ang")
	else:
		raise Exception("Wrong number of arguments")
	
	result = '_y_spt_afterframes {} "_y_spt_setangles {} {}"'.format(frame, x_ang, y_ang)
	return result, frame