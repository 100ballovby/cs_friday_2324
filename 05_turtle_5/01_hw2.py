from turtle import *


def draw_circle(obj, x, y, rad, ext=360):
    obj.up()
    obj.goto(x, y)
    obj.down()
    obj.circle(rad, ext)


t = Turtle()
t.speed(0)

x = -100
rad = 30
t.pensize(rad * 0.15)
for i in range(10):
    draw_circle(t, x, 0, rad)
    x += rad * 2

t.up()
t.goto(-100, 60)
t.down()
t.fd(rad * 18)

done()