def swap(a, b):
	tmp = a
	a = b
	b = tmp
	return a, b


def string_bubble_sort(string):
	char_list = list(string)  # превращаю строчку в список
	for i in range(len(char_list) - 1):
		for j in range(len(char_list) - 1 - i):
			if char_list[j] > char_list[j + 1]:
				char_list[j], char_list[j + 1] = swap(char_list[j], char_list[j + 1])
	sorted_string = ''.join(char_list)  # последовательное сложение каждого элемента списка с пустой строкой
	return sorted_string


s = 'zanbykloce'
res = string_bubble_sort(s)
print(res)
