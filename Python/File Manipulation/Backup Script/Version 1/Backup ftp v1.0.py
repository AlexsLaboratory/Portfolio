from ftplib import FTP
import sys, ftplib

sys.tracebacklimit = 0 # Does not display traceback errors
sys.stderr = "/dev/null" # Does not display Attribute errors

Host = "ftp.debian.org"
Port = 21
Username = ""
Password = ""

def MainClass():
	global ftp
	global con
	Host
	Port
	ftp = FTP()
	con = ftp.connect(Host, Port) # Connects to the host with the specified port

def grabfile():
	source = "/debian/"
	filename = "README.html"
	ftp.cwd(source)
	localfile = open(filename, 'wb')
	ftp.retrbinary('RETR ' + filename, localfile.write)
	ftp.quit()
	localfile.close()

try:
	MainClass()
except Exception:
	print("Not Connected")
	print("Check the address", Host + ":" + str(Port))
else:
	print("Connected")

if ftplib.error_perm and not Username == "" and Password == "":
	print("Please check your credentials\n", Username, "\n", Password)

credentials = ftp.login(Username, Password)
grabfile()