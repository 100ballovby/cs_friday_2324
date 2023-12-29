from turtle import *


t = Turtle()
t.speed(1)

for i in range(4):
    t.fd(100)
    t.lt(90)

t.goto(50, 50)

for i in range(4):
    t.fd(100)
    t.lt(90)

# нижняя правая сторона
t.goto(150, 50)
t.goto(100, 0)

# верхняя правая сторона
t.goto(100, 100)
t.goto(150, 150)

# верхняя левая сторона
t.goto(50, 150)
t.goto(0, 100)


done()