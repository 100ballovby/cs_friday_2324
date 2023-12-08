from turtle import *


def x_angle(obj, angles, length, x, y, col):
    """
    Рисует многоугольник, получая количество углов, которое
    в нем должно быть.
    :param obj: черепашка
    :param angles: количество углов многоугольника
    :param length: длина стороны
    :param x: координата х
    :param y: координата у
    :param col: цвет
    :return: None
    """
    obj.up()
    obj.goto(x, y)
    obj.down()
    obj.color(col)
    deg = 360 / angles
    for i in range(angles):
        obj.fd(length)
        obj.left(deg)


t = Turtle()
t.speed(0)

x_angle(t, 4, 100, 100, 100, 'red')
x_angle(t, 3, 100, -100, -100, 'red')
x_angle(t, 5, 100, 200, -310, 'red')
x_angle(t, 6, 100, -250, 100, 'red')
x_angle(t, 35, 5, 250, 100, 'red')
x_angle(t, 12, 15, -300, -200, 'red')


done()
