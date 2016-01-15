import os, datetime

now = datetime.datetime.now()
Year = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
Time = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)

directoryName = Year + " " + Time

if not os.path.isdir("./" + directoryName + "/"):
  os.mkdir("./" + directoryName + "/")
