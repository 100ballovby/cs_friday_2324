import datetime as dt


def is_leap(year):
	if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
		return True
	else:
		return False


now = dt.datetime.now()
res = is_leap(now.year)
print(f'{now.year} is leap year: {res}')



