import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", user="use", passwd="pass", db="Hob1", port=3306)
cursor = db.cursor()
cursor.execute("SELECT text FROM Statuses")

for x in each cursor

print('cursor')

cursor.close()
db.close()
sys.exit()
