from turtle import *

t = Turtle()

t.circle(50)  # нарисовать окружность с радиусом 50
t.dot(100)  # нарисовать круг с диаметром 100 (радиус 50)

for i in range(10):
    t.circle(25, 180)  # рисуем полукруг
    t.lt(180)  # поворачиваем влево на 180


t.up()
t.goto(-200, 200)
t.down()

for i in range(50):
    t.circle(50)
    t.rt(6)

done()
