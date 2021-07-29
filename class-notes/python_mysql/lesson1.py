# -*- coding: utf-8 -*-

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
cur.execute("select * from author where author_id like '%S%'")

# 実行結果を取得
rows = cur.fetchall()

# 実行結果の表示する
for row in rows:
    print(row)

# 件数を取得する
print(cur.rowcount, "件、取得しました")


# カーソルを切断
cur.close()
#
conn.close()
