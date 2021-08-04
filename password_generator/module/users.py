# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 14:39:09 2021

@author: user24
"""

import mysql.connector as mydb

cursor = mydb.cursor()

class Users:
    users = []
    def __init__(self, user):
        self._user = user
    
    def add_user():
        name = input("Enter you name: ")
        login = input("Enter you login(email): ")
        password1 = input("Enter you password: ")
        password2 = input("Enter your password again")
        
        while password1 != password2:
            print("Passwords don't match. Try again.")
            password1 = input("Enter you password: ")
            password2 = input("Enter your password again")
            
        data = (login, password1, name)
        cur.execute("insert into users (login, password, name) values(%s, %s)", data)
        conn.commit()
        print("登録しました。")
                
    
    def login():
        pass
    
    def logout():
        pass
    