def ending(string):
	if len(string) >= 3:
		if string.endswith('ing'):
			string = string.replace('ing', 'ly')
			return string
		string += 'ing'
		return string
	return string


def ending_v2(string):
	end = string[-3:]
	s = string[:-3]
	if len(string) >= 3:
		if end == 'ing':
			s += 'ly'
			return s
		string += 'ing'
		return string
	return string


res = ending('le')
res2 = ending_v2('lettering')
print(res2)
