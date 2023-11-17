from turtle import *


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

done()
