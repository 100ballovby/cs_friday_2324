"""Посчитать сумму элементов списка рекурсивно"""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def rec_sum(array):
    # базовый случай: если список пуст
    if not array:  # если array не существует
        return 0
    # рекурсивный случай: складываю первый элемент и вызов функции для остального списка
    return array[0] + rec_sum(array[1:])


print(rec_sum(l))




