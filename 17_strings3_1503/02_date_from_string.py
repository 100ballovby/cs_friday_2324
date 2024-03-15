import datetime as dt


my_date = input('Введите дату: ')
new_date = dt.date.fromisoformat(my_date)
print(new_date)
print(new_date.day + 20)
