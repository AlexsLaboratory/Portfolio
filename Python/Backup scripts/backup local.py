from subprocess import call
import os, datetime, time, sys

Source = "/Users/alowe/Desktop/testdir2"
Destination = "/Users/alowe/Desktop/testdir"

nowDatetime = datetime.datetime.now()
Year = str(nowDatetime.month) + "-" + str(nowDatetime.day) + "-" + str(nowDatetime.year) # Sets current Year to month, day, and year
Time = str(nowDatetime.hour) + ":" + str(nowDatetime.minute) + ":" + str(nowDatetime.second) # Sets current Time to hour, minute, and second
directoryName = Year + " " + Time # Combines Name, Year, and Time

if os.path.exists(Destination) == False: # if the destination does not exists then create the destination
	os.makedirs(Destination)
else:
	print("Directory already exists", Destination)

os.chdir(Destination)
os.mkdir(directoryName)

# call(["mkdir", Destination])
# call(["mkdir", directoryName])
# call(["cd", Destination])
# call(["cd", directoryName])

call(["cp" , "-r", Source, directoryName])
