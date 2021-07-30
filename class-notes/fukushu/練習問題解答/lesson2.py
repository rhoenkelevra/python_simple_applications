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

# 著者IDの入力
id = input("author_idを入力してください：")

# SQL文の実行
cur.execute("select * from author where author_id = '" + id + "'")

# 実行結果を取得
rows = cur.fetchall()

if cur.rowcount > 0:
    # 実行結果の表示
    for row in rows:
        print(row)
else:
    print("未登録です。")

# カーソルの切断
cur.close()

# コネクションの切断
conn.close()