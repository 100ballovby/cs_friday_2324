import datetime as dt


def print_delta(delta):
	years = delta.days // 365
	remaining_days = delta.days % 365
	month = remaining_days // 30
	days = remaining_days % 30

	res = f'{years} years, {month} months, {days} days left.'
	return res

# x years, x month, x day, x hours, x minutes left
day = dt.datetime(2024, 8, 16)
now = dt.datetime.now()
print(print_delta(day - now))
