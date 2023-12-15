from turtle import *


t = Turtle()
t.speed(1)
t.shape('turtle')

for i in range(8):
    t.fd(100)
    t.stamp()
    t.rt(180)
    t.fd(100)
    t.rt(180)
    t.rt(45)

t.hideturtle()  # спрятать черепашку на экране

done()
