# task 1
for i in range(1, 101):
    if i % 2 == 0:
        print(i, end=', ')

print()
# task 2
summ = 0
for i in range(1, 101):
    summ += i
print('Сумма чисел от 1 до 100:', summ)