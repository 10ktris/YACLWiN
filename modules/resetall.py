def resolve(args, frame):
	if args:
		raise Exception("Wrong number of arguments")
	result =  '_y_spt_afterframes {} "-attack"\n'.format(frame)
	result += '_y_spt_afterframes {} "-attack2"\n'.format(frame)
	result += '_y_spt_afterframes {} "-duck"\n'.format(frame)
	result += '_y_spt_afterframes {} "-jump"\n'.format(frame)
	result += '_y_spt_afterframes {} "-back"\n'.format(frame)
	result += '_y_spt_afterframes {} "-forward"\n'.format(frame)
	result += '_y_spt_afterframes {} "-moveleft"\n'.format(frame)
	result += '_y_spt_afterframes {} "-moveright"\n'.format(frame)
	result += '_y_spt_afterframes {} "-use"\n'.format(frame)
	result += '_y_spt_afterframes {} "_y_spt_pitchspeed 0"\n'.format(frame)
	result += '_y_spt_afterframes {} "_y_spt_yawspeed 0"'.format(frame)
	return result, frame