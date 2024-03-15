import datetime as dt


target_date = dt.datetime(2024, 3, 15, 16, 50)
now_date = dt.datetime.now()
while now_date <= target_date:
	print(target_date - now_date)
	now_date = dt.datetime.now()

print(type(target_date - now_date))  # timedelta - разница между двумя датами (или временами)



