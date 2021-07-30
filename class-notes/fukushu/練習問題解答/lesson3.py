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

while True:
    # 処理の選択
    cmd = input("1)author\t2)category\t3)books\t9)終了:")
    # コマンドによって処理を分ける
    if cmd == "1":
        sql = "select * from author"
    elif cmd == "2":
        sql = "select * from category"
    elif cmd == "3":
        sql = "select * from books"
    elif cmd == "9":
        break
    else:
        continue

    # SQL文の実行
    cur.execute(sql)

    # 実行結果を取得
    rows = cur.fetchall()

    # 実行結果の表示
    for row in rows:
        print(row)

# カーソルの切断
cur.close()

# コネクションの切断
conn.close()