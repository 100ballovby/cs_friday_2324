from turtle import *


def draw_triangle(obj, x, y, length, angle=120):
    obj.up()
    obj.goto(x, y)
    obj.down()
    for i in range(3):
        obj.fd(length)
        obj.rt(angle)


t = Turtle()
t.speed(0)

t.fillcolor("cyan")
t.begin_fill()
draw_triangle(t, -200, -200, 400, -120)
t.end_fill()
t.fillcolor("green")
t.begin_fill()
draw_triangle(t, -100, -25, 200, 120)
t.end_fill()

done()

