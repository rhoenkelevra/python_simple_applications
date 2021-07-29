# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 11:56:03 2021

@author: user24
"""
import mysql.connector as mydb

conn = mydb.connect(
    host="localhost",
    port="3306",
    user="rhoen",
    password="pass",
    database="book"
)

cur = conn.cursor()

res = cur.fetchall()
for row in res:
    print(row)

print(conn.is_connected())

# Put this close on the finally part of the try block
# so even if there is an error, the connection will be closed
cur.close()
conn.close()
