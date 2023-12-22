from turtle import *


def spider(obj, length, q):
    for i in range(q):
        obj.fd(length)
        for j in range(3):
            obj.fd(length * 0.3)
            obj.rt(120)
        obj.rt(180)
        obj.fd(length)
        obj.rt(180)
        obj.rt(360 / q)

t = Turtle()
t.speed(0)
t.shape('turtle')

spider(t, 100, 200)

t.hideturtle()  # спрятать черепашку на экране

done()
