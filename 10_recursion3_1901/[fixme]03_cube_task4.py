"""
Дано число n, найти его куб
"""
def cube(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n * cube(n - 1)


print(cube(5))

