from turtle import *


t = Turtle()
t.speed(0)


def lines(obj, length, x, y, direction):
    for i in range(length // 10):  # количество повторений должно быть целым числом
        obj.up()
        obj.goto(x, y)
        obj.down()
        obj.fd(length)
        length *= 0.9
        y -= direction  # -= - вниз, += - вверх


lines(t, 200, 0, 0, 10)
lines(t, 200, 0, 0, -10)

done()
