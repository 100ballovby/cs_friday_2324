def count_letters(string):
	count = 0
	for i in range(len(string)):
		if string[i].isalpha():
			count += 1
	return count


def count_signs(string):
	count = 0
	for i in range(len(string)):
		if string[i] == '.' or string[i] == ',' or string[i] == '!' or string[i] == '?':
			count += 1
	return count


def count_signs_v2(string):
	count = 0
	for i in range(len(string)):
		if string[i] in '.,!?':  # Работает только в Python
			count += 1
	return count


res = count_letters("Hello, 123 3 ! + 0-")
print(res)
res2 = count_signs("Hello, World! I'm, . ! ?")
res3 = count_signs_v2("Hello, World! I'm, . ! ?")
print(res2)
print(res3)
