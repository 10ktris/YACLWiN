def resolve(args, frame):
	if len(args) == 1:
		duration = args[0]
		if type(duration) != int:
			raise TypeError("Wrong type argument")
	else:
		raise Exception("Wrong number of arguments")
	return "", frame + duration