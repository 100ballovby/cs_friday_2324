from turtle import *
import random as r

t = Turtle()
t.pensize(5)
t.color('blue')
t.speed(0)
t.shape('turtle')

# нарисовать квадрат
for i in range(4):
    t.fd(100)
    t.rt(90)

# нарисовать треугольник
t.color('pink')
for i in range(3):
    t.fd(100)
    t.lt(120)

t.up()  # перестать рисовать (поднять перо)
t.goto(-150, 310)  # перейти в х: -150, у: 310
t.down()  # начать рисовать (опустить перо)

# нарисовать прямоугольник
t.color('cyan')
for i in range(2):
    t.fd(400)
    t.rt(90)
    t.fd(200)
    t.rt(90)


for i in range(100):  # повторить 100 раз
    x = r.randint(-450, 450)  # сгенерировать случайную координату х
    y = r.randint(-450, 450)  # сгенерировать случайную координату у
    t.up()
    t.goto(x, y)  # перейти в случайные координаты
    t.down()
    t.lt(r.randint(-180, 180))  # повернуться в случайном направлении
    t.stamp()  # делает "отпечаток" черепашки

done()

