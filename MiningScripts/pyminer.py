import MySQLdb
import sys
import Location_Call
import socket
import os
import subprocess

def main():

    db = MySQLdb.connect(host="localhost", user="use", passwd="pass", db="Hob1", port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT text FROM Statuses")

    for x in cursor:
	tweet = cursor.fetchone()
	line = str(tuple(tweet)).translate(None, '!@$('')')
	tweetsplit = split_line(line)
	#print tweetsplit
	tup = str(tuple(tweetsplit))
	#print tup
	cmd = ('python Location_Call.py -q ') + tweetsplit + "'"
	#os.system("Location_Call.py cursor.fetchone()")
	subproc = subprocess.Popen(cmd, shell=True)
    cursor.close()
    db.close()
    sys.exit()

def split_line(text):
    words = text.split()
    for word in words:
        return word

if __name__=="__main__":
    main()



