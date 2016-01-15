#!/usr/local/bin/python3

import time
from subprocess import call
from datetime import datetime

while True:
	print("-------- Time Until Christmas --------")
	print("")

	Datetime = datetime.now()
	Month0 = 12 - Datetime.month
	Day0 = 31 - Datetime.day
	Hour0 = 24 - Datetime.hour
	Minute0 = 60 - Datetime.minute
	Second0 = 60 - Datetime.second

	Month = str(Month0) + " " + "Month"
	Day =  str(Day0) + " " + "Day"
	Hour = str(Hour0) + " " + "Hour"
	Minute = str(Minute0) + " " + "Minute"
	Second = str(Second0) + " " + "Second"

	Date0 = [Month]
	Date1 = [Day]
	Date2 = [Hour]
	Date3 = [Minute]
	Date4 = [Second]


	for str0 in Date0:
		if (str0 != str(0) + " " + "Month"):
			if (Month0 > 1):
				if (Month0 <= 9):
					print("------------")
					print("|" + " " + str0 + "s" + " " + "|")
					print("------------")
				else:
					print("-------------")
					print("|" + " " + str0 + "s" + " " + "|")
					print("-------------")
			elif (Month0 <= 9):
				print("-----------")
				print("|" + " " + str0 + " " + "|")
				print("-----------")

	for str1 in Date1:
		if (str1 != str(0) + " " + "Day"):
			if (Day0 > 1):
				if (Day0 <= 9):
					print("----------")
					print("|" + " " + str1 + "s" + " " + "|")
					print("----------")
				else:
					print("-----------")
					print("|" + " " + str1 + "s" + " " + "|")
					print("-----------")
			elif (Day0 <= 9):
				print("---------")
				print("|" + " " + str1 + " " + "|")
				print("---------")

	for str2 in Date2:
		if (str2 != str(0) + " " + "Hour"):
			if (Hour0 > 1):
				if (Hour0 <= 9):
					print("-----------")
					print("|" + " " + str2 + "s" + " " + "|")
					print("-----------")
				else:
					print("------------")
					print("|" + " " + str2 + "s" + " " + "|")
					print("------------")
			elif (Hour0 <= 9):
				print("----------")
				print("|" + " " + str2 + " " + "|")
				print("----------")

	for str3 in Date3:
		if (str3 != str(0) + " " + "Minute"):
			if (Minute0 > 1):
				if (Minute0 <= 9):
					print("-------------")
					print("|" + " " + str3 + "s" + " " + "|")
					print("-------------")
				else:
					print("--------------")
					print("|" + " " + str3 + "s" + " " + "|")
					print("--------------")
			elif (Minute0 <= 9):
				print("------------")
				print("|" + " " + str3 + " " + "|")
				print("------------")

	for str4 in Date4:
		if (str4 != str(0) + " " + "Second"):
			if (Second0 > 1):
				if (Second0 <= 9):
					print("-------------")
					print("|" + " " + str4 + "s" + " " + "|")
					print("-------------")
				else:
					print("--------------")
					print("|" + " " + str4 + "s" + " " + "|")
					print("--------------")
			elif (Second0 <= 9):
				print("------------")
				print("|" + " " + str4 + " " + "|")
				print("------------")
			time.sleep(1)
			# call(["clear"])
