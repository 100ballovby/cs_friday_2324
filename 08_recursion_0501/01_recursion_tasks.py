# Напишите функцию, которая находит n-й член последовательности Фибоначчи.

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(3))
