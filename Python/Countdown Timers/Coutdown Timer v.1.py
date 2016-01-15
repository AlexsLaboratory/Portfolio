#!/usr/local/bin/python3.5

import time, datetime
from subprocess import call

Year = 2015
Month = 12
Day = 30
Hour = 4
Minute = 18
Second = 50

while True:
	# Datetime = datetime.datetime(Year, Month, Day, Hour, Minute, Second)
	Datetime = datetime.datetime(2018, 1, 3, 5, 5, 5)
	diff = Datetime - datetime.datetime.now()
	diff = str(diff)

	day_str, not_useful, time_str = diff.split()

	time_str = str(time_str)

	hour_str, minute_str, second = time_str.split(":")

	second = str(second)
	second_str, not_useful = second.split(".")

	years = int(day_str) / float(365)

	years0, year_fraction = divmod(years, 1)
	years0 = int(years0)
	Year0 = str(years0)

	days0 = round(year_fraction * 365.25)
	days0 = int(days0)
	Day0 = str(days0)

	Year1 = Year0 + " " + "Year" # Year
	Day1 = Day0 + " " + "Day" # Day
	Hour1 = hour_str + " " + "Hour" # Hour
	Minute1 = minute_str + " " + "Minute" # Min
	Second1 = second_str # Sec

	Date0 = [Year1]
	Date1 = [Day1]
	Date2 = [Hour1]
	Date3 = [Minute1]
	Date4 = [second_str]


	for str0 in Date0:
		if (str0 != str(0) + " " + "Year"):
			if (str(Year0) == str("01")):
				print("-" * 10)
				print("|" + " " + str0 + " " + "|")
				print("-" * 10)
			else:
				print("-" * 11)
				print("|" + " " + str0 + "s" + " " + "|")
				print("-" * 11)

	for str1 in Date1:
		if (str1 != str(0) + " " + "Day"):
			if (str(day_str) == str("01")):
				print("-" * 9)
				print("|" + " " + str1 + " " + "|")
				print("-" * 9)
			else:
				print("-" * 12)
				print("|" + " " + str1 + "s" + " " + "|")
				print("-" * 12)

	for str2 in Date2:
		if (str2 != str(0) + " " + "Hour"):
			if (str(hour_str) == str("01")):
				print("----------")
				print("|" + " " + str2 + " " + "|")
				print("----------")
			else:
				print("-" * 12)
				print("|" + " " + str2 + "s" + " " + "|")
				print("-" * 12)

	for str3 in Date3:
		if (str3 != str(0) + " " + "Minute"):
			if (str(minute_str) == str("01")):
				print("----------")
				print("|" + " " + str3 + " " + "|")
				print("----------")
			else:
				print("-" * 14)
				print("|" + " " + str3 + "s" + " " + "|")
				print("-" * 14)

	if second_str <= str("09"):
		second_str = second_str[1]

	for str4 in Date4:
		if (str4 != str(0) + " " + "Second"):
			if (str(second_str) == str("1")):
				print("-" * 13)
				print("|" + " " + second_str + " " + "Second" + " " + "|")
				print("-" * 13)
			else:
				print("-" * 14)
				print("|" + " " + second_str + " " + "Seconds" + " " + "|")
				print("-" * 14)

	print(str4)
	print(second_str)
	print(Date4)
	time.sleep(1)