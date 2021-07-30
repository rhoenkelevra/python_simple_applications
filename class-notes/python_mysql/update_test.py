# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 09:11:32 2021

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

# 更新する情報を準備
data = ("キタミ リュウジ", "K0002") # jap. space insert weird char \u3000
update = "update author set name_kana = %s where author_id = %s"

# SQL 文の実行
cur.execute(update, data)


# 件数を取得する
print(cur.rowcount, "件、更新しました")

# 更新を確定する
conn.commit()

# カーソルとコネクションを切断
cur.close()
conn.close()
