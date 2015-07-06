def resolve(args, frame):
	if len(args) == 1:
		angular_speed = args[0]
		if type(angular_speed) not in (int, float):
			raise TypeError("Wrong type argument : angular_speed")
	else:
		raise Exception("Wrong number of arguments")
	result = '_y_spt_afterframes {} "_y_spt_yawspeed {}"'.format(frame, angular_speed)
	return result, frame