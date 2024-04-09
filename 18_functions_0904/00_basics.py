def count_symbols(string):
	res = 0
	for char in string:  # перебираю каждый элемент строки
		res += 1
	return res




k = '3o'
print(count_symbols(k))
