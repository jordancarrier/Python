#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector as mariadb

def executeSQL(conn, queryTerm):
    cursor = conn.cursor()
    query = "select ASIN, Description from Amazon where Description like " + queryTerm
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
       print row[0], row[1]

hostname = 'localhost'
username = 'python'
password = 'pythonpass123'
database = 'python'

try:
   sys.argv[1]
except IndexError:
   print "Error - missing query word! Usage ./findBook queryWord"
   sys.exit(1)
else:
   queryWord = "'%" + sys.argv[1] + "%'"

connection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
executeSQL(connection,queryWord)
connection.close()

#insert
#try:
#    cursor.execute("INSERT INTO interface_id (paket_id,data_id) VALUES (%s,%s)", ('Maria','DB'))
#except mariadb.Error as error:
#    print("Error: {}".format(error))

#mariadb_connection.commit()
#print "The last inserted id was: ", cursor.lastrowid

#mariadb_connection.close()