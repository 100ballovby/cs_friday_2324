"""
Напишите программу, которая проверяет, является ли строка палиндромом.
Строка передается через аргумент функции.
"""
s = 'казаки'

for i in range(len(s) // 2):
    if s[i] != s[-i - 1]:
        print(False)
        break