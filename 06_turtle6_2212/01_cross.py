from turtle import *


def cross(obj, length, x, y):
    obj.up()
    obj.goto(x, y)
    obj.down()
    for i in range(4):
        obj.fd(length)
        obj.rt(90)
        obj.fd(length)
        obj.rt(90)
        obj.fd(length)
        obj.lt(90)


def curve_cross(obj, length, x, y):
    obj.up()
    obj.goto(x, y)
    obj.down()
    for i in range(3):
        obj.rt(120)
        obj.fd(length)
        obj.rt(90)
        obj.fd(length)
        obj.lt(90)
        obj.fd(length)

t = Turtle()
t.speed(1)

curve_cross(t, 100, 0, 0)

done()

