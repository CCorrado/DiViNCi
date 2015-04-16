import MySQLdb
import sys
import time
import Location_Call
import socket
import os
import subprocess
import nltk

def main():

    db = MySQLdb.connect(host="localhost", user="use", passwd="pass", db="Hob1", port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT text FROM Statuses")
    cursor2 = db.cursor()
    cursor2.execute("SELECT created_at FROM Statuses")
    cursor3 = db.cursor()
    cursor3.execute("SELECT user_id FROM Statuses")

    for x in cursor:
	tweetobj = []
	x = cursor.fetchone()
	#print x
	date = cursor2.fetchone()
	#print date
	user = cursor3.fetchone()
	#print user
	line = str(tuple(x)).translate(None, '!@/("RT")u:""$('')')
	#print line
	tweetsplit = split_line(line)
	count = 0
	n = 0
	for n in range(0, len(tweetsplit)):
	    #print tweetsplit[n]
	    #tup = str(list(tweetsplit))
	    #print tup
	    cmd = ('python Location_Call.py -q ') + tweetsplit[n] + "'"
	    #print x, user, date
            subproc = subprocess.Popen(cmd, shell=True)
	    n = n + 1
            #time.sleep(0.5)

    cursor.close()
    cursor2.close()
    db.close()
    sys.exit()

def split_line(text):
    words = nltk.word_tokenize(text)
    #for word in words:
    return words

if __name__=="__main__":
    main()



