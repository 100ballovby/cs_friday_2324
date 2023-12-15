import random as r
import string


def colors(num):
    cols = []
    alph = string.hexdigits  # шестнадцатиричный алфавит
    for i in range(num):
        col = '#'
        for j in range(6):  # 6 раз
            col += r.choice(alph)  # добавить случайный символ из алфавита
        cols.append(col)  # добавляем цвет в список
    return cols  # возвращаем список цветов


