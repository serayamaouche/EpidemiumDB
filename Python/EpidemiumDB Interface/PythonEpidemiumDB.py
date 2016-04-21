 #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Script File: PythonEpidemiumDB.py  
# Date of creation: 21 avril 2016
# Date of last modification: 22 avril 2016
# Author: Seraya Maouche <seraya.maouche@iscb.org>
# Project: EpidemiumDB (http://www.epidemium.cc)
# Short Description: This script provides functionalities to access 
#                     EpidemiumDB in Python using MySQLdb
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Python MySQL interface
# Python DB-API is Python' standard for database interfaces. MySQL is supported
# by this API.
# The DB API provides a minimal standard for working with databases. 

# You can use MySQLdb which provides an interface for connecting to a 
# MySQL server from Python.

# Install MySQLdb
#!/usr/bin/python
import MySQLdb
# Open database connection
db = MySQLdb.connect(host="host_name",    # host name (IP address for Epidemium.cc)
                     user="username",     # your username
                     passwd="password",   # your password
                     db="epidemiumdb")    # name of the database


# Prepare a cursor object using cursor()
cursor = db.cursor()

# Send and SQL query using execute()
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone()
data = cursor.fetchone()
print "Database version : %s " % data

cursor.execute("SELECT * FROM metadata")
rows = cursor.fetchall()

# Print rows
for row in rows:
    print row

for row in cursor.fetchall():
    print row[0]


# Disconnect from server
db.close() 

