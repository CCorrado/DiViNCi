from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(host="localhost", user="use", passwd="pass", db="Hob1", port=3306)
cursor = cnx.cursor()

day = datetime.now().date()
#+ timedelta(days=1)

add_location = ("INSERT INTO locations "
               "(location, x, y, magniutde, entry_date) "
               "VALUES (%s, %s, %s, %s, %s)")
add_salary = ("INSERT INTO locations "
              "(loc, x, y, mag) "
              "VALUES (%(loc)s, %(x)s, %(y)s, %(magnitude)s)")

f = open('TWEETmined', 'w')

for line in f:
    tweet_data = (%s, %s, %s, , date(1977, 6, 14))

	# Insert new location
    cursor.execute(add_location, tweet_data)
    loc = cursor.lastrowid

	# Insert location information
    tweet_data = {
      'loc': loc,
      'x': 50000,
      'y': tomorrow,
      'magnitude': mag,
    }
cursor.execute(add_location, tweet_data)

# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()
