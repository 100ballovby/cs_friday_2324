import string as s
import random as r
from turtle import *

t = Turtle()
t.shape('turtle')
t.speed(0)

colors = []
q = 1500

for color in range(q):
    color = '#'  # здесь хранится цвет
    for i in range(6):  # повторить 6 раз
        sym = r.choice(s.hexdigits)  # выбрать случайный символ
        color += sym  # добавить символ к цвету
    colors.append(color)  # добавляю цвет в список


t.pensize(5)
for i in range(1000):
    t.color(r.choice(colors))  # установка случайного цвета пера черепашки
    x = r.randint(-400, 400)  # случайная координата для черепашки
    y = r.randint(-400, 400)  # случайная координата для черепашки
    rad = r.randint(40, 100)  # радиус круга, который будем рисовать
    t.dot(rad)  # рисую круг
    t.up()  # поднимаю перо
    t.goto(x, y)  # перехожу в новые координаты
    t.down()  # опускаю перо


done()
