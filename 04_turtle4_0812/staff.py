def draw_circle(obj, x, y, rad, ext=360):
    obj.up()
    obj.goto(x, y)
    obj.down()
    obj.circle(rad, ext)



