import pytz
import datetime as dt


def convert_time(time, from_tz, to_tz):
	from_zone = pytz.timezone(from_tz)  # превращаю название часового пояса в объект
	to_zone = pytz.timezone(to_tz)  # превращаю название часового пояса в объект

	utc_time = pytz.utc.localize(dt.datetime.strptime(time, '%H:%M:%S'))  # сохраняю время как объект времени
	utc_time.replace(tzinfo=from_zone).astimezone(to_zone)
	# ^ меняю старый часовой пояс на новый часовой пояс
	converted_time = utc_time.astimezone(to_zone)
	return converted_time.strftime('%H:%M:%S')

time = dt.datetime.today().strftime('%H:%M:%S')
from_tz = 'Europe/Moscow'
to_tz = 'US/Eastern'
conv = convert_time(time, from_tz, to_tz)
print(f'Time in Minsk: {time}.')
print(f'Time in East coast US: {conv}.')




