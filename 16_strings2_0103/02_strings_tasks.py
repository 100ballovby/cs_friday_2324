def remove_char(string, n):
	first_part = string[:n]
	last_part = string[n+1:]

	return first_part + last_part


def remove_replace(string, n):
	string = string.replace(string[n], '')
	return string


def remove_nth_char(string, n):
	new_string = ''
	for i in range(len(string)):
		if (i + 1) % n != 0:
			new_string += string[i]
	return new_string



print(remove_nth_char('abcdefghijklmnopqrstuvwxyz', 2))
print(remove_nth_char('abcdefghijklmnopqrstuvwxyz', 5))
