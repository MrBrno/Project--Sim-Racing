from datetime import datetime
import subprocess, sqlite3, time

def getParameters():
	conn = sqlite3.connect("../project_sim_racing/db.sqlite3")
	c = conn.cursor()
	#get raceMinute from website database
	#get track from website database
	#get car from website database
	conn.close()

def writeToServer(car, track):
	with open("../servers/Series1/Server1/cfg/server_cfg.ini", "w") as f:
		f.writelines("") #Clear the document
	with open("../servers/Series1/Server1/cfg/enty_list.ini", "w") as f:
			f.writelines("") #Clear the document
	with open("../servers/Series1/Server1/cfg/server_cfg.ini", "w") as f:
		f.writelines("") #Clear the document
	with open("../servers/Series1/Server1/cfg/enty_list.ini", "w") as f:
			f.writelines("") #Clear the document

	with open("../servers/Series1/Server1/cfg/enty_list.ini", "a") as f:
		for i in range(0, 19):
						f.writelines("[CAR_" + str(i) + "]\n")
						f.writelines("MODEL=" + car + "\n")
						f.writelines("SKIN=" + "\n")
						f.writelines("SPECTATOR_MODE=0" + "\n")
						f.writelines("DRIVERNAME=" + "\n")
						f.writelines("TEAM=" + "\n")
						f.writelines("GUID=" + "\n")
						f.writelines("Ballast=" + "\n")
						f.writelines("\n")

	with open("../servers/Series1/Server2/cfg/enty_list.ini", "a") as f:
		for i in range(0, 19):
						f.writelines("[CAR_" + str(i) + "]\n")
						f.writelines("MODEL=" + car + "\n")
						f.writelines("SKIN=" + "\n")
						f.writelines("SPECTATOR_MODE=0" + "\n")
						f.writelines("DRIVERNAME=" + "\n")
						f.writelines("TEAM=" + "\n")
						f.writelines("GUID=" + "\n")
						f.writelines("Ballast=" + "\n")
						f.writelines("\n")

#def startServer():
	#if minute = raceMinute-1:
		#subprocess.run(['../servers/Series1/Server1/acServer.exe'])
		#subprocess.run(['../servers/Series1/Server2/acServer.exe'])

while True:
	getParameters()
	writeToServer(car, )
	#startServer()
	time.sleep(5)