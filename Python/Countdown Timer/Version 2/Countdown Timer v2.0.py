#!/usr/local/bin/python3.5

import time, datetime
from subprocess import call

Year = 2016
Month = 1
Day = 9
Hour = 1
Minute = 1
Second = 1

while True:
	Datetime = datetime.datetime(Year, Month, Day, Hour, Minute, Second)
	diff = Datetime - datetime.datetime.now()
	diff = str(diff)

	day_str, not_useful, time_str = diff.split()
	hour_str, minute_str, second = time_str.split(":")
	second_str, not_useful = second.split(".")

	years = int(day_str) / 365

	print(diff)

	year_final, year_fraction = divmod(years, 1)
	int_year_final = int(year_final)
	str_years_final = str(int_year_final)

	rounded_days = round(year_fraction * 365.25)
	int_days_final = int(rounded_days)
	str_days_final = str(int_days_final)

	Date0 = [str_years_final]
	Date1 = [str_days_final]
	Date2 = [hour_str]
	Date3 = [minute_str]
	Date4 = [second_str]

	if (int_year_final != 0):
		if str_years_final <= str("9"):
			str_years_final = str(str_years_final[1])

	for str0 in Date0:
		if (str0 != str(0)):
			if (str(str_years_final) == str("1")):
				print("-" * 10)
				print("|" + " " + str_years_final + " " + "Year" + " " + "|")
				print("-" * 10)
			else:
				print("-" * 13)
				print("|" + " " + str_years_final + " " + "Years" + " " + "|")
				print("-" * 13)

	if (int_days_final != 0):
		if str_days_final <= str("09"):
			str_days_final = str(str_days_final[1])

	for str1 in Date1:
		if (str1 != str(0)):
			if (str(str_days_final) == str("1")):
				print("-" * 9)
				print("|" + " " + str_days_final + " " + "Day" + " " + "|")
				print("-" * 9)
			else:
				print("-" * 12)
				print("|" + " " + str_days_final + " " + "Days" + " " + "|")
				print("-" * 12)

	if (int(hour_str) != 0):
		if hour_str <= str("09"):
			hour_str = str(hour_str[1])

	for str2 in Date2:
		if (hour_str != str(0)):
			if (str(hour_str) == str("1")):
				print("-" * 10)
				print("|" + " " + hour_str + " " + "Hour" + " " + "|")
				print("-" * 10)
			else:
				print("-" * 12)
				print("|" + " " + hour_str + " " + "Hours" + " " + "|")
				print("-" * 12)

	if (int(minute_str) != 0):
		if minute_str <= str("09"):
			minute_str = str(minute_str[1])

	for str3 in Date3:
		if (minute_str != str(0)):
			if (str(minute_str) == str("1")):
				print("-" * 12)
				print("|" + " " + minute_str + " " + "Minute" + " " + "|")
				print("-" * 12)
			else:
				print("-" * 14)
				print("|" + " " + minute_str + " " + "Minutes" + " " + "|")
				print("-" * 14)

	if (int(second_str) != 0):
		if second_str <= str("09"):
			second_str = str(second_str[1])

	for str4 in Date4:
		if (str(second_str) == str("1")):
			print("-" * 13)
			print("|" + " " + second_str + " " + "Second" + " " + "|")
			print("-" * 13)
		else:
			print("-" * 14)
			print("|" + " " + second_str + " " + "Seconds" + " " + "|")
			print("-" * 14)

	if (str_years_final == 0 and str_days_final == 0 and hour_str == 0 and minute_str == 0 and second_str == 0):
		break

	# Date0 = [str_years_final]
	# Date1 = [str_days_final]
	# Date2 = [hour_str]
	# Date3 = [minute_str]
	# Date4 = [second_str]

	time.sleep(1)