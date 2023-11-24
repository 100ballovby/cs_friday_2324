from turtle import *


t = Turtle()  # объект, который рисует
t.shape('turtle')  # выбрать форму "черепашка"
t.speed(0)

side = 10

for square in range(10):
    for line in range(4):  # квадрат рисуется здесь
        t.fd(side)
        t.rt(90)
    t.fd(side)  # идем вперед на длину квадрата


done()  # предотавращает закрытие окна черепашки после запуска
# ниже, чем done() не может быть НИЧЕГО
