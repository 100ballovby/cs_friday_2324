import datetime as dt


now = dt.datetime.now()
tomorrow = dt.timedelta(days=1)
yesterday = dt.timedelta(days=-1, hours=4, seconds=-7200)
print(now + tomorrow)
print(now + yesterday)

