from turtle import *


t = Turtle()
t.pensize(5)  # толщина линии черепашки (больше 10 ставить бессмысленно)
t.color('blue')  # цвет линии, которую рисует черепашка
t.speed(0)  # скорость черепашки. 0 - самая быстрая
t.shape('turtle')

t.fd(100)
t.rt(45)
t.color('brown')
t.fd(-150)

done()
