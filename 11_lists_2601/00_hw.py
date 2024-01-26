"""
Написать программу, которая определит, является ли число n простым
1. получаем число n
2. Организуем цикл for в диапазоне от 2 до значения n, деленного на 2
3. Находим количество делителей числа. При помощи условия проверяем,
делится ли число без остатка и если да, увеличиваем счетчик на единицу
5. Если число делителей равно 0, то проверяемое число является простым
"""


def is_prime(n):  # рекурсия тоже должна будет возвращать либо True, либо False
    if n == 1 or n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        return is_prime(n // 2)


print(is_prime(12))