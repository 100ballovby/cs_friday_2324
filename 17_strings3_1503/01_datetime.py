import datetime as dt


date = dt.date(year=2024, month=3, day=15)  # формирует дату
print(date)
time = dt.time(hour=16, minute=20, second=13)  # формирует время
print(time)
together = dt.datetime(year=2024, month=3, day=15, hour=16, minute=20, second=13)  # формирует объект datetime
print(together)

print(dt.date.today())  # создает сущность с текушей локальной датой (берет из ОС)
print(dt.datetime.now())  # создает сущность с текущей локальной датой и временем

now = dt.datetime.now()
current_time = dt.time(now.hour, now.minute)
print(current_time)
