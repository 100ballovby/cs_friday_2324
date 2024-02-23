def length(string):
	count = 0
	for _ in string:  # если управляющая переменная цикла не используется, ее принято называть _
		count += 1
	return count


def both_ends(string):
	if len(string) < 2:
		return ''

	return string[0:2] + string[-2:]


def change_char(string):
	first_char = string[0]
	string = string.replace(first_char, '$')
	str = first_char + string[1:]
	return str


def char_mix_up(a, b):
	new_a = b[:1] + a[1:]
	new_b = a[:1] + b[1:]
	res = new_a + ' ' + new_b
	return res


print(char_mix_up('abc', 'xyz'))

s = 'Hello, world!'
for i in range(length(s)):
	print(s[i])

print(both_ends('hello'))
print(both_ends('k'))
print(both_ends('w3school'))

print(change_char('abracadabra'))

