#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='python', password='pythonpass123', database='python')
cursor = mariadb_connection.cursor()

#insert
try:
    cursor.execute("INSERT INTO interface_id (paket_id,data_id) VALUES (%s,%s)", ('Maria','DB'))
except mariadb.Error as error:
    print("Error: {}".format(error))

mariadb_connection.commit()
print "The last inserted id was: ", cursor.lastrowid

mariadb_connection.close()