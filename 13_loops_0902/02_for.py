n = int(input('Number: '))

for i in range(1, 11):  # последовательность 1, 2, ... 9, 10
    print(n, '*', i, '=', n * i)


############### на while
count = 1
while (count <= 10):
    print(n, '*', count, '=', n * count)
    count += 1

"""
Любую задачу, написанную циклом for можно переписать на while,
но в обратную сторону это работает не всегда.
"""
