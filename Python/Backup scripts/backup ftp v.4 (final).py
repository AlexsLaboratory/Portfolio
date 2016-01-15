from subprocess import call
import os, datetime, time, sys, shutil

# Setup ####################################
Username = os.environ["Username"] # Username for the ftp server
Password = os.environ["Password"] # Password for the ftp server
Archive = os.environ["Archive"]
Site = os.environ["Site"] # FTP site url
Source = os.environ["Source"] # Path on the FTP server
Destination = os.environ["Destination"] # Location on the your computer to download files
#############################################

# Options ###################################
Name = "" # Adds a name to downloaded files
Npf = "off" # Turns on or off --no-passive-ftp
Nhd = "off" # Turns on or off --no-host-directories
Nc = "off" # Turns on or off --no-clobber
Num = "" # --cut-dirs list
List = "" # --exclude-directories list
#############################################

linux = sys.platform.startswith('linux')
darmin = sys.platform.startswith('darmin')
os2 = sys.platform.startswith('os2')

if linux == linux or darmin == darmin or os2 == os2: # Makes sure that this scropt is running on one of these OS's 

	if os.path.exists(Destination) == False: # if the destination does not exists then create the destination
		os.makedirs(Destination)
	else:
		print("Directory already exists", Destination)

	nowDatetime = datetime.datetime.now()
	Year = str(nowDatetime.month) + "-" + str(nowDatetime.day) + "-" + str(nowDatetime.year) # Sets current Year to month, day, and year
	Time = str(nowDatetime.hour) + "-" + str(nowDatetime.minute) + "-" + str(nowDatetime.second) # Sets current Time to hour, minute, and second
	directoryName = Name + "" + Year + " " + Time # Combines Name, Year, and Time

	Url = Site + Source

	if Username and Password == " ":
		Url = "ftp://" + Url
	else:
		Url = "ftp://" + Username + ":" + Password + "@" + Site + ":21" + "/" + Source

	os.mkdir(Destination + "/" + directoryName + "/")
	os.chdir(Destination + "/" + directoryName)

	if Npf == "on":
		Npf = "--no-passive-ftp"
	elif Npf == "off":
		Npf = "--passive-ftp"

	if Nhd == "on":
		Nhd = "--no-host-directories"
	elif Nhd == "off":
		Nhd = "--host-directories"

	if Nc == "on":
		Nc = "--no-clobber"
	elif Nc == "off":
		Nc = "--clobber"

	Cd = "--cut-dirs=" + Num
	Ed = "--exclude-directories=" + List

	def backUp(Source):
		call(["wget", "-r",Ed ,Cd ,Nc ,Nhd ,Npf ,Source])

	backUp(Url)

	call(["7z", "a", "-t7z", directoryName + ".7z", Destination + "/" + directoryName, "-mx9", "-mmt", "-ms", "-p" + Archive])
	shutil.move(directoryName + ".7z", Destination)
	shutil.rmtree(Destination + "/" + directoryName)

	nowTime = time.time()
	for file in os.listdir(Destination):
		file = os.path.join(Destination, file)
		if os.stat(os.path.join(Destination, file)).st_mtime <= nowTime - 30 * 86400:
			if os.path.isfile(file):
				os.remove(os.path.join(Destination, file))
else:
	print("This script is not supported on", sys.platform) # Runs if you are not running one of the supported OS's
