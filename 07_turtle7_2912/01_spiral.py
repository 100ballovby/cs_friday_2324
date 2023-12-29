from turtle import *
from math import *


def spiral(obj, rad, ang, turn):
    for i in range(turn * 360 // ang):
        obj.fd(ang * pi / 180 * rad)
        t.lt(ang)
        rad += 0.3

t = Turtle()
t.speed(0)

spiral(t, 3, 9, 5)

done()

