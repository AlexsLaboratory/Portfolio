#!/usr/local/bin/python3.5

import time, datetime
from subprocess import call

Year = 2016
Month = 1
Day = 15
Hour = 13
Minute = 0
Second = 0

target_date = datetime.datetime(Year, Month, Day, Hour, Minute, Second)
timedelta_zero = datetime.timedelta(0)

while True:
	diff = target_date - datetime.datetime.now()
	diff_str = str(diff)

	if (len(diff_str) >= int(21)):
		identifacation = int(1)
		day_str, not_useful, time_str = diff_str.split()
		hour_str, minute_str, second = time_str.split(":")
		second_str, not_useful = second.split(".")
	else:
		identifacation = int(2)
		hour_str, minute_str, second = diff_str.split(":")
		second_str, not_useful = second.split(".")

	if (diff <= timedelta_zero):
		break
	time.sleep(1)

	if (identifacation == int(1)):

		years = int(day_str) / float(365)

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


	# if (int(int_year_final) != int(0)):
		if str_years_final <= str("9"):
			str_years_final = str(str_years_final)

		for str0 in Date0:
			if (str0 != str(0)):
				if (str(str_years_final) == str("1")):
					outline = "-" * 10
					years = "|" + " " + str_years_final + " " + "Year" + " " + "|"

					print(outline)
					print(years)
					print(outline)
				else:
					years = "|" + " " + str_years_final + " " + "Years" + " " + "|"

					outline = "-" * len(years)

					print(outline)
					print(years)
					print(outline)

	# # if (int(int_days_final) != int(0)):
	# 	if int_days_final <= int(9):
	# 		str_days_final = str(str_days_final[1])

		for str1 in Date1:
			if (str1 != str(0)):
				if (str(str_days_final) == str("1")):
					outline = "-" * 9
					days = "|" + " " + str_days_final + " " + "Day" + " " + "|"

					print(outline)
					print(days)
					print(outline)
				else:
					days = "|" + " " + str_days_final + " " + "Days" + " " + "|"

					outline = "-" * len(days)

					print(outline)
					print(days)
					print(outline)

	# if (int(hour_str) != int(0)):
		if int(hour_str) <= int(9):
			hour_str = str(hour_str)

		for str2 in Date2:
			if (hour_str != int(0)):
				if (int(hour_str) == int(1)):
					outline = "-" * 10
					hours = "|" + " " + hour_str + " " + "Hour" + " " + "|"

					print(outline)
					print(hours)
					print(outline)
				else:
					hours = "|" + " " + hour_str + " " + "Hours" + " " + "|"

					outline = "-" * len(hours)

					print(outline)
					print(hours)
					print(outline)

	# if (int(minute_str) != int(0)):
		if minute_str <= str("09"):
			minute_str = str(minute_str[1])

		for str3 in Date3:
			if (int(minute_str) != int(0)):
				if (int(minute_str) == int(1)):
					outline = "-" * 12
					minutes = "|" + " " + minute_str + " " + "Minute" + " " + "|"

					print(outline)
					print(minutes)
					print(outline)
				else:
					minutes = "|" + " " + minute_str + " " + "Minutes" + " " + "|"
					
					outline = "-" * len(minutes)

					print(outline)
					print(minutes)
					print(outline)


	# if (int(second_str) != int(0)):
		if (second_str) <= str("09"):
			second_str = str(second_str[1])

		for str4 in Date4:
			if (int(second_str) == int(1)):
				outline = "-" * 12
				seconds = "|" + " " + second_str + " " + "Second" + " " + "|"

				print(outline)
				print(seconds)
				print(outline)
			else:
				seconds = "|" + " " + second_str + " " + "Seconds" + " " + "|"

				outline = "-" * len(seconds)

				print(outline)
				print(seconds)
				print(outline)

	elif (identifacation == int(2)):

		Date2 = [hour_str]
		Date3 = [minute_str]
		Date4 = [second_str]

	# # if (int(hour_str) != int(0)):
	# 	if hour_str <= str("09"):
	# 		hour_str = str(hour_str)

		for str2 in Date2:
			if (int(hour_str) != int(0)):
				if (int(hour_str) == int(1)):
					outline = "-" * 10
					hour = "|" + " " + hour_str + " " + "Hour" + " " + "|"

					print(outline)
					print(hour)
					print(outline)
				else:
					outline = "-" * 11
					hours = "|" + " " + hour_str + " " + "Hours" + " " + "|"

					outline = "-" * len(hours)

					print(outline)
					print(hours)
					print(outline)

	# if (int(minute_str) != int(0)):
		if minute_str <= str("09"):
			minute_str = str(minute_str[1])

		for str3 in Date3:
			if (int(minute_str) != int(0)):
				if (int(minute_str) == int(1)):
					outline = "-" * 12
					minutes = "|" + " " + minute_str + " " + "Minute" + " " + "|"

					print(outline)
					print(minutes)
					print(outline)
				else:
					outline = "-" * 14
					minutes = "|" + " " + minute_str + " " + "Minutes" + " " + "|"
					
					outline = "-" * len(minutes)

					print(outline)
					print(minutes)
					print(outline)

	# if (int(second_str) != int(0)):
		if int(second_str) <= int(9):
			second_str = str(second_str[1])

		for str4 in Date4:
			if (int(second_str) == int(1)):
				outline = "-" * 12
				seconds = "|" + " " + second_str + " " + "Second" + " " + "|"

				print(outline)
				print(seconds)
				print(outline)
			else:
				seconds = "|" + " " + second_str + " " + "Seconds" + " " + "|"

				outline = "-" * len(seconds)

				print(outline)
				print(seconds)
				print(outline)
print("Time is up")