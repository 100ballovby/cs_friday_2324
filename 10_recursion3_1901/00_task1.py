# возведение числа в степень
def power(n, p):
    if p == 0:
        return 1
    else:  # рекурсивный случай
        return n * power(n, p - 1)


print(power(9, 3))
