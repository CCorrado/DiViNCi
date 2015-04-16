import MySQLdb
import sys
import time
import Location_Call
import socket
import os
import subprocess

def main():

    db = MySQLdb.connect(host="localhost", user="use", passwd="pass", db="Hob1", port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT text FROM Statuses")
    cursor2 = db.cursor()
    cursor2.execute("SELECT created_at FROM Statuses")
    cursor3 = db.cursor()
    cursor3.execute("SELECT user_id FROM Statuses")

    for x in cursor:
	x = cursor.fetchone()
	#print x
	date = cursor2.fetchone()
	#print date
	user = cursor3.fetchone()
	#print user
	line = str(tuple(x)).translate(None, '!@(''RT'')(''('')('')'')"$('')')
	#print line
	tweetsplit = split_line(line)
	#print tweetsplit
	#tup = str(tuple(tweetsplit))
	#print tup
	cmd = ('python Location_Call.py -q ') + tweetsplit + "'"
	#os.system("Location_Call.py cursor.fetchone")
	print x, user, date
	print tweetsplit
	subproc = subprocess.Popen(cmd, shell=True)
	time.sleep(0.1)
    cursor.close()
    cursor2.close()
    db.close()
    sys.exit()

def split_line(text):
    words = text.split()
    for word in words:
        return word

if __name__=="__main__":
    main()



