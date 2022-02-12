from datetime import datetime
import subprocess,time,sqlite3

class server:
	def __init__(self):
		#SQL Database for race scheduling - Will eventually be a dedicated app for setting up events
		self.conn = sqlite3.connect("races.db") # This is self so it can be used from every place in this code
		self.c = self.conn.cursor()
		#c.execute("""CREATE TABLE races (
		#            time text,
		#            car text,
		#            track text
		#            )""")

		self.c.execute(
			"INSERT INTO races VALUES ('2245', 'mazda_mx5_cup', 'magione')")

		self.c.execute(
			"DELETE FROM races WHERE rowid in (select rowid FROM races LIMIT 1)")

		self.c.execute("SELECT time FROM races")
		self.raceTime = self.c.fetchone()
		self.c.execute("SELECT car FROM races")
		self.car = self.c.fetchone()
		self.car = self.car[0]
		self.c.execute("SELECT track FROM races")
		self.track = self.c.fetchone()
		self.track = self.track[0]

		print("The next race is: " + self.car + " at " + self.track + " at " + self.raceTime[0])

		self.conn.commit()
		self.conn.close()

		self.start_server()
	def start_server(self):
		#Starts the server
		while True:
			now = datetime.now()
			currentTime = now.strftime("%H%M")
			#print(int(raceTime[0])-1-int(currentTime))
			# Server startup 1 minute before scheduled time.
			if int(currentTime) == int(self.raceTime[0])-1:

				with open("cfg/server_cfg.ini", "r") as f:
					data = f.readlines()

				data[2] = "CARS=" + self.car + "\n"  # Set Server Car
				data[4] = "TRACK=" + self.track + "\n"  # Set Server Track

				with open("cfg/server_cfg.ini", "w") as f:
					f.writelines(data)  # Push changes to server CFG files

				with open("cfg/entry_list.ini", "w") as f:  # Clear Entry List
					f.writelines("")

				# Write every individual car to the entry list CFG file
				with open("cfg/entry_list.ini", "w") as f:
					for i in range(0, 24):
						f.writelines("[CAR_" + str(i) + "]\n")
						f.writelines("MODEL=" + self.car + "\n")
						f.writelines("SKIN=" + "\n")
						f.writelines("SPECTATOR_MODE=0" + "\n")
						f.writelines("DRIVERNAME=" + "\n")
						f.writelines("TEAM=" + "\n")
						f.writelines("GUID=" + "\n")
						f.writelines("Ballast=" + "\n")
						f.writelines("\n")

				subprocess.run(['acServer.exe'])  # Runs the dedicated server
				# Prevents the server from running more than once - not sure this is necassary
				time.sleep(5)
				self.c.execute("DELETE FROM races WHERE rowid in (select rowid FROM races LIMIT 1)")

server = server() 