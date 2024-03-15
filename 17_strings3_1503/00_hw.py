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


def sort_list_string(lst):
	for i in range(len(lst) - 1):
		for j in range(len(lst) - 1 - i):
			if len(lst[j]) > len(lst[j + 1]):
				lst[j], lst[j + 1] = swap(lst[j], lst[j + 1])
	return lst


l1 = ['ertwert', 'wawe', 'nan', '', '21', '43462378190459874', '14923', 'zl']
sorted_l1 = sort_list_string(l1)
print(sorted_l1)

for i in range(len(sorted_l1)):
	sorted_l1[i] = string_bubble_sort(sorted_l1[i])

print(sorted_l1)
