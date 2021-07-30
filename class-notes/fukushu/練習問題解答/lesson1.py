import mysql.connector as mydb

# コネクションの作成
conn = mydb.connect(
    host="localhost",
    port="3306",
    user="user",
    password="pass",
    database="book"
)

# カーソルの作成
cur = conn.cursor()

# SQL文の実行
cur.execute("select * from author where author_id like 'S%'")

# 実行結果を取得
rows = cur.fetchall()

# 実行結果の表示
for row in rows:
    print(row)

# カーソルの切断
cur.close()

# コネクションの切断
conn.close()