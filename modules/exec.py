def resolve(args, frame):
	if len(args) == 1:
		name = args[0]
		

	else:
		raise Exception("Wrong number of arguments")
	
	result  = '_y_spt_afterframes {} "exec" + name \n'.format(frame)
	return result, frame