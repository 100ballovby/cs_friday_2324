from turtle import *
from staff import colors
import random as r


t = Turtle()
t.speed(0)
col_list = colors(10000)

for i in range(5000):
    x = r.randint(-500, 500)
    y = r.randint(-500, 500)
    d = r.randint(20, 80)
    t.color(r.choice(col_list))
    t.up()
    t.goto(x, y)
    t.down()
    t.dot(d)


done()
