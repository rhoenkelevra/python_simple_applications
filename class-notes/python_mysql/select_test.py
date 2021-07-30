# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 11:41:06 2021

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

# ＳＬＱ文の実行
query = "select * from category"
cur.execute(query)

# 実行結果を取得
rows = cur.fetchall()

# 実行結果の表示する
for row in rows:
    print(row)

# 件数を取得する
print(cur.rowcount, "件、取得しました")

# カーソルとコネクションを切断
cur.close()
conn.close()
