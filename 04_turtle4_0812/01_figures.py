from turtle import *
from staff import draw_circle


t = Turtle()
t.speed(0)

draw_circle(t, 100, 100, 50)
t.rt(90)
x = -150
for i in range(15):
    draw_circle(t, x, 150, 20, -180)
    x += 40
    t.lt(180)

rounds = 120
for i in range(rounds):
    draw_circle(t, 80, 0, 50)
    t.rt(360 / rounds)


done()
