def square(obj, length, width, x, y, col):
    obj.up()
    obj.goto(x, y)
    obj.down()
    obj.color(col)
    obj.fillcolor(col)
    obj.begin_fill()
    for i in range(2):
        obj.fd(length)
        obj.rt(90)
        obj.fd(width)
        obj.rt(90)
    obj.end_fill()