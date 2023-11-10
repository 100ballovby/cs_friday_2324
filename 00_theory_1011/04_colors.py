import string as st
import random as r

colors = []
q = int(input('How many colors? '))

for color in range(q):
    color = '#'  # здесь хранится цвет
    for i in range(6):  # повторить 6 раз
        sym = r.choice(st.hexdigits)  # выбрать случайный символ
        color += sym  # добавить символ к цвету
    colors.append(color)  # добавляю цвет в список

print(colors)