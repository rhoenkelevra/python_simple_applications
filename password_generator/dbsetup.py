# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 13:29:57 2021

@author: user24
"""

import mysql.connector as mydb
from mysql.connector import errorcode

con = mydb.connect(
    host="localhost",
    port="3306",
    user="root",
    password="rfr689022",
    database="passwords"
)

cursor = con.cursor(buffered=True)

TABLES = {}

TABLES['users'] = (
    "CREATE TABLE `users` ("
    "  `user_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `login` varchar(255) NOT NULL,"
    "  `password` varchar(255) NOT NULL,"
    "  `name` varchar(255) NOT NULL,"
    "  `date created` timestamp DEFAULT CURRENT_TIMESTAMP,"
    "  `d_flag` tinyint(1) DEFAULT 1,"
    "  PRIMARY KEY (`user_id`)"
    ") ENGINE=InnoDB")

TABLES['passwords'] = (
    "CREATE TABLE `passwords` ("
    "  `pass_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `user_id` int(11) NOT NULL,"
    "  `login` varchar(255) NOT NULL,"
    "  `password` varchar(255) NOT NULL,"
    "  `notes` varchar(255),"
    "  `date_created` timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,"
    "  `d_flag` tinyint(1) DEFAULT 1,"
    "  PRIMARY KEY (`pass_id`),"
    "  FOREIGN KEY (user_id) REFERENCES `users` (`user_id`)"
    ") ENGINE=InnoDB")


for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mydb.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


cursor.close()
con.close()
