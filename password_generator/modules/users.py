# -*- coding: utf-8 -*-
import mysql.connector as mydb
import typing
from modules.connector import connect as cnn


cursor = cnn.cursor()


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
        cursor.execute(
            "insert into users (login, password, name) values(%s, %s)", data)
        cnn.commit()
        print("登録しました。")

    def login():
        pass

    def logout():
        pass
