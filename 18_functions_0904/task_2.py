import datetime as dt

# написать программу, которая определяет номер недели в году по дате
date = input('Введите дату ДД.ММ.ГГГГ: ').split('.')
print(dt.date(int(date[2]), int(date[1]), int(date[0])).isocalendar()[1])

