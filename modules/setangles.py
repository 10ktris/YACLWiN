def resolve(args, frame):
	if len(args) == 2:
		x_angle = args[0]
		y_angle = args[1]
		if type(x_angle) not in (int, float):
			raise TypeError("Wrong type argument : x_angle")
		if type(y_angle) not in (int, float):
			raise TypeError("Wrong type argument : y_angle")
	else:
		raise Exception("Wrong number of arguments")
	
	result =  '_y_spt_afterframes {} "_y_spt_setpitch {}"\n'.format(frame, y_angle)
	result += '_y_spt_afterframes {} "_y_spt_setyaw {}"'.format(frame, x_angle)
	return result, frame