import datetime, time

while True:
	Datetime = datetime.datetime(2016, 12, 30, 5, 5, 5)
	diff = Datetime - datetime.datetime.now()
	diff = str(diff)

	day_str, not_useful, time_str = diff.split()

	time_str = str(time_str)

	hour_str, minute_str, second = time_str.split(":")

	second = str(second)
	second_str, not_useful = second.split(".")

	if day_str <= str("09"):
		day_str = day_str[1]
		print(day_str)
	else:
		print(day_str)

	if hour_str <= str("09"):
		hour_str = hour_str[1]
		print(hour_str)
	else:
		print(hour_str)

	if minute_str <= str("09"):
		minute_str = minute_str[1]
		print(minute_str)
	else:
		print(minute_str)

	if second_str <= str("09"):
		second_str = second_str[1]
		print(second_str)
	else:
		print(second_str)


	time.sleep(1)
