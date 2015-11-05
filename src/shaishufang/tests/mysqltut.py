#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "archer", "archer", "shaishufang")

# Prepare a cursor object using cursor() method
cursor = db.cursor()

# Execute SQL query using execute method
cursor.execute("select VERSION()")

# Fetch a single row using fetchone() method
data = cursor.fetchone()

print "Database version: %s " % data

# disconnect from server
db.close()
