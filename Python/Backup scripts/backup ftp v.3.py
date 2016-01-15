from subprocess import call 
import os, datetime

now = datetime.datetime.now()
Year = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
Time = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)

directoryName = Year + " " + Time

Destination = "/Users/alowe/Desktop/testdir/" + directoryName
Options = "r"
def backUp(Source):
	call(["wget", "-" + Options, "-P" + Destination, Source])

backUp("ftp://ftp.debian.org/*")



