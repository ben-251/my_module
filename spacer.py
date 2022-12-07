def get_spacings(iterables):
	# space out based on length of longest one,
	# making that one have a spacing of one to the next one
	#
	# then check the ends of the next iterable and repeat

	for iterable in iterables:
		longest_string_length = max(map(len, iterable))
		for string in iterable:
			spacing_for_string = get_spacing(string,longest_string_length)
			spacing
		