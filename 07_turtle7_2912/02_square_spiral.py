from turtle import *


def spiral(obj, count, angle):
    length = 5
    for i in range(count):
        obj.fd(length)
        obj.rt(360 / angle)
        length += 5


t = Turtle()
t.speed(0)

spiral(t, 50, 12)

done()
