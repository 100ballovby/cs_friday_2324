import datetime as dt


x = dt.datetime.now()
y = x + dt.timedelta(0, 5)
print(x.time())
print(y.time())
