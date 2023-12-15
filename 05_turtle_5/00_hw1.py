from turtle import *


def draw_circle(obj, x, y, rad, ext=360):
    obj.up()
    obj.goto(x, y)
    obj.down()
    obj.circle(rad, ext)


t = Turtle()
t.speed(0)

x = -350
rad = 80
t.pensize(rad * 0.15)
for i in range(4):
    draw_circle(t, x, 0, rad)
    x += rad * 1.4

done()