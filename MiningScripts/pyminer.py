# Purpose: Python Script to mine tweets exported to a SQL database based on tokenized sentences
# Requirements:
# 1. MySQL database with tweets running on local machine or other (see db conn string)
# 2. Location_Call.py python script, based on the Yelp API 

# Author: Christopher L. Corrado
# CCorrads@gmail.com
# Senior Design CpE 424 Group 14 
# DiViNCi: Digital Hoboken
# May 5th, 2015

# Import libraries required 
# (many can be easily installed in Linux with "pip install #library" or "apt-get install python-#library")
import MySQLdb
import sys
import time
import Location_Call
import socket
import os
import subprocess
import nltk

#define main function
def main():

#set varialbes for MySQL Database calls and connections
    db = MySQLdb.connect(host="localhost", user="use", passwd="pass", db="Hob1", port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT text FROM Statuses")
    cursor2 = db.cursor()
    cursor2.execute("SELECT created_at FROM Statuses")
    cursor3 = db.cursor()
    cursor3.execute("SELECT user_id FROM Statuses")

#iterate through database utilizing database cursors assigned to the tweet, the date, and the author
    for x in cursor:
	tweetobj = []
	x = cursor.fetchone()
	#print x
	date = cursor2.fetchone()
	#print date
	user = cursor3.fetchone()
	#print user
#cast the tweet tuple into a string to define a line
	line = str(tuple(x)).translate(None, '!@/("RT")u:""$('')')
	#print line
#call the split line function to tokenize the casted line
	tweetsplit = split_line(line)
	count = 0
	n = 0
	for n in range(0, len(tweetsplit)):
	    #print tweetsplit[n]
	    #tup = str(list(tweetsplit))
	    #print tup
	    cmd = ('python Location_Call.py -q ') + tweetsplit[n] + "'"
	    #print x, user, date
#spoof a terminal session (reason for unterminated string syntax error, some tweets have "'" char at end)
            subproc = subprocess.Popen(cmd, shell=True)
	    n = n + 1
#unnecessary sleep, good for presentation
            time.sleep(0.1)
#close database cursors
    cursor.close()
    cursor2.close()
    db.close()
    sys.exit()

# Function to define the sentence "tokenizing" calling the NLTK library function "word_tokenize".
# More can be found on NLTK at www.nltk.org
# Admittedly, This function needs more work. We want to return specific words (nouns, proper nouns, etc)

def split_line(text):
    words = nltk.word_tokenize(text)
    #for word in words:
    return words

# standard python syntax for calling this script in a terminal or from another script,
# i.e. if another script uses this file, the default function call is main.
if __name__=="__main__":
    main()
