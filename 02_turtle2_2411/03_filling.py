from turtle import *

t = Turtle()

long = 200
short = 140

t.fillcolor("brown")
t.color("brown")
t.begin_fill()
for i in range(2):  # рисуем сам дом
    t.fd(long)
    t.rt(90)
    t.fd(short)
    t.rt(90)
t.end_fill()

t.fillcolor("bisque")
t.color("bisque")
t.begin_fill()
for i in range(3):
    t.fd(long)
    t.lt(120)
t.end_fill()

t.fillcolor("blue")
t.color("blue")
t.up()  # перемещаю черепашку ниже и правее для рисования окна
t.goto(20, -35)  # перемещаю черепашку ниже и правее для рисования окна
t.down()  # перемещаю черепашку ниже и правее для рисования окна
t.begin_fill()
for i in range(2):  # рисуем сам дом
    t.fd(long * 0.4)
    t.rt(90)
    t.fd(short * 0.3)
    t.rt(90)
t.end_fill()

t.fillcolor("coral")
t.color("coral")
t.up()  # перемещаю черепашку ниже и правее для рисования окна
t.goto(long - (long * 0.3), 0 - (short * 0.4))  # перемещаю черепашку ниже и правее для рисования окна
t.down()  # перемещаю черепашку ниже и правее для рисования окна
t.begin_fill()
for i in range(2):  # рисуем сам дом
    t.fd(long * 0.25)
    t.rt(90)
    t.fd(short * 0.6)
    t.rt(90)
t.end_fill()


done()
