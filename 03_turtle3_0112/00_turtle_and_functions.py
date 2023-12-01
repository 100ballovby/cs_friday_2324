from turtle import *
from draw_functions import square  # функции можно хранить в другом файле и импортировать


t = Turtle()
t.speed(0)


house_x = 0
house_y = -50

square(t, 1000, 600, -500, 500, 'blue')  # небо
square(t, 1000, 400, -500, -100, 'green')  # земля
square(t, 230, 190, house_x, house_y, 'brown')  # коробка дома
square(t, 90, 78, house_x + 20, house_y - 50, 'cyan')  # окно


done()

