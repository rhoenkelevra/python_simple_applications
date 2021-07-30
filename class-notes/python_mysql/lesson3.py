# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 09:27:40 2021

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

#　カーソルの作成
cur = conn.cursor()

while True:
    ans = input("1) author\t2) category\t3)books\t9) 終了\n--> ")
    
    # if ans == "1":
    #     query = "select * from author"
    # elif ans == "2":
    #     query = "select * from category"
    # elif ans == "3":
    #     query = "select * from books"
    # elif ans == "9":
    #     break
    # else:
    #     print("Not available")
    #     continue
    

    if ans == "1":
        data = ("author",)
    elif ans == "2":
        data = ("category",)
    elif ans == "3":
        data = ("books",)
    elif ans == "9":
        break
    else:
        print("Not available")
        continue
    # ＳＬＱ文の実行
    
    query = "select * from %s"
    cur.execute(query, data)

    # 実行結果を取得
    rows = cur.fetchall()

    # 実行結果の表示する
    for row in rows:
        print(row)

    # 件数を取得する
    print(cur.rowcount, "件、取得しました")

# カーソルを切断
cur.close()
conn.close()
