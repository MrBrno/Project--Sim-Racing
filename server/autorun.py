import subprocess
import sqlite3
from datetime import datetime
import time

#SQL Database for race scheduling - Will eventually be a dedicated app for setting up events
conn = sqlite3.connect("races.db")
c = conn.cursor()

#c.execute("""CREATE TABLE races (
#            time text,
#            car text,
#            track text
#            )""")

c.execute("INSERT INTO races VALUES ('1856', 'mazda_mx5_cup', 'magione')")

c.execute("DELETE FROM races WHERE rowid in (select rowid FROM races LIMIT 1)")

c.execute("SELECT time FROM races")
raceTime = c.fetchone()
c.execute("SELECT car FROM races")
car = c.fetchone()
car = car[0]
c.execute("SELECT track FROM races")
track = c.fetchone()
track = track[0]

print("The next race is: " + car + " at " + track + " at " + raceTime[0])

conn.commit()
conn.close()



#Starts the server
while True:
    now = datetime.now()
    currentTime = now.strftime("%H%M")
    #print(int(raceTime[0])-1-int(currentTime))
    if int(currentTime) == int(raceTime[0])-1: #Server startup 1 minute before scheduled time.

        with open("cfg/server_cfg.ini", "r") as f:
            data = f.readlines()

        data[2] = "CARS=" + car + "\n" #Set Server Car
        data[4] = "TRACK=" + track + "\n" #Set Server Track

        with open("cfg/server_cfg.ini", "w") as f:
            f.writelines(data) #Push changes to server CFG files


        with open("cfg/entry_list.ini", "w") as f: #Clear Entry List
            f.writelines("")

        with open("cfg/entry_list.ini", "w") as f: #Write every individual car to the entry list CFG file
            for i in range(0, 24):
                f.writelines("[Car_" + str(i) + "]\n")
                f.writelines("MODEL=" + car + "\n")
                f.writelines("SKIN=" + "\n")
                f.writelines("SPECTATOR_MODE=0" + "\n")
                f.writelines("DRIVERNAME=" + "\n")
                f.writelines("TEAM=" + "\n")
                f.writelines("GUID=" + "\n")
                f.writelines("Ballast=" + "\n")
                f.writelines("\n")
        
        subprocess.run(['acServer.exe']) #Runs the dedicated server
        time.sleep(5) #Prevents the server from running more than once - not sure this is necassary
        c.execute("DELETE FROM races WHERE rowid in (select rowid FROM races LIMIT 1)")