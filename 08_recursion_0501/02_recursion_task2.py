# Напишите функцию, которая выводит все цифры числа N в обратном порядке.

def reverse_digits(n):
    number = 0
    while n > 0:
        remainder = n % 10  # записываю последнюю цифру числа
        n //= 10  # уменьшаю n на один разряд (десятков)
        if number > 0:  # если в итоговое число уже записали цифру
            number *= 10
            number += remainder
        else:
            number += remainder

    return number


res = reverse_digits(31894)
print(type(res))  # int


def rev_dig_recursion(n):
    if n == 0:
        return ''
    else:
        return str(n % 10) + str(rev_dig_recursion(n // 10))


res = rev_dig_recursion(31894)
print(type(res))  # str
res = int(res)
print(type(res))

