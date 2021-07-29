# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 11:19:23 2021

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

print(conn.is_connected())

conn.close()
