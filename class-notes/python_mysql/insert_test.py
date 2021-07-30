# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 09:11:19 2021

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

# 登録する情報を準備
data = ("Y0002", "山田 太郎", "ヤマダ タロウ") # jap. space insert weird char \u3000
insert = "insert into author values(%s, %s, %s)"

# SQL 文の実行
cur.execute(insert, data)


# 件数を取得する
print(cur.rowcount, "件、取得しました")

# 更新を確定する
conn.commit()

# カーソルとコネクションを切断
cur.close()
conn.close()
