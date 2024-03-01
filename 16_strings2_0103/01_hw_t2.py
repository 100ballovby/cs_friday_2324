def longest(string_list) -> tuple:
	longest = ''
	for i in range(len(string_list)):
		if len(string_list[i]) > len(longest):
			longest = string_list[i]
	return longest, len(longest)


s = ['lorem', 'ipsum', 'dolor', 'sit', 'amet', 'hello, world', 'i am developer', 'nope']
longest_string, longest_length = longest(s)
print(f'String: {longest_string}\nLength: {longest_length}')

