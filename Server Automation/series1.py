from datetime import datetime
import subprocess, sqlite3, time

def getParameters():
	conn = sqlite3.connect("../project_sim_racing/db.sqlite3")
	c = conn.cursor()
	#get raceMinute from website database
	#get track from website database
	#get car from website database
	#conn.close()

#def startServer():
	#if minute = raceMinute-1:
		#subprocess.run(['server1/acServer.exe'])
		#subprocess.run(['server2/acServer.exe'])

while True:
	getParameters()
	print()
	#startServer()
	time.sleep(5)