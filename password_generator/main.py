# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 14:33:35 2021

@author: user24
"""
# from modules.users import Users
# from modules.password import Passwords
from modules.connector import connect

# import flask
import mysql.connector as mydb


con = connect()
cur = con.cursor()

q = cur.execute("select * from books")
rows = cur.fetchall()

for row in rows:
    print(row)



cur.close()
con.close()


# welcome
#  menu 1) login 2) sign up
# login screen
# input login and pass
#

# Login Screen
# welcome message
# menu: 1) add new 2) show all 3)search 0)logoff
# 1. login, pass, notes
# pass -> 1. from user 2. generatte

# 3. search by login
# after finding it:
# 1) back 2) edit 3) erase
