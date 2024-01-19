"""
Дано число N, необходимо найти сумму его цифр

25 = 2 + 5
389 = 3 + 8 + 9
4921 = 4 + 9 + 2 + 1
"""


def sum_digits(n):
    res = 0
    while n != 0:
        res += n % 10
        n //= 10
    return res


def sum_digits_r(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits_r(n // 10)


print(sum_digits(937))
print(sum_digits_r(937))



