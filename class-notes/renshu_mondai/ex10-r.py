import mysql.connector as mydb

conn = None
cur = None

#データベース接続
def dbConnection():
    global conn
    global cur
    conn = mydb.connect(host="localhost",port="3306",user="user",password="pass",database="ex11")
    cur = conn.cursor()

#スケジュール追加
def addSchedule(note,date):
    dbConnection()
    data = (note,date)
    cur.execute("insert into schedule values(null,%s,%s)",data)
    if cur.rowcount > 0:
        conn.commit()
        print("登録しました。")
    else:
        print("登録できませんでした。")
    cur.close()
    conn.close()

#スケジュール修正
def updateSchedule(note,date,id):
    dbConnection()
    data = (note,date,id)
    checkDate = (id,)
    cur.execute("select * from schedule where id = %s",checkDate)
    rows = cur.fetchall()
    if cur.rowcount > 0:
        cur.execute("update schedule set note = %s , date = %s where id = %s",data)
        if cur.rowcount > 0:
            conn.commit()
            print("修正しました。")
        else:
            print("修正できませんでした。")
    else:
        print("入力されたスケジュール番号は存在しませんでした。")
    cur.close()
    conn.close()

#スケジュール削除
def deleteSchedule(id):
    dbConnection()
    data = (id,)
    cur.execute("delete from schedule where id = %s",data)
    if cur.rowcount > 0:
        conn.commit()
        print("削除しました。")
    else:
        print("削除できませんでした。")
    cur.close()
    conn.close()

#スケジュール全件表示
def allShowSchedule():
    dbConnection()
    cur.execute("select * from schedule")
    rows = cur.fetchall()
    if cur.rowcount > 0:
        for row in rows:
            print("ID："+str(row[0]))
            print("日時："+str(row[2]))
            print("スケジュール："+str(row[1]))
            print()
    else:
        print("スケジュールが見つかりませんでした。")
    cur.close()
    conn.close()

#スケジュール指定表示
def showSchedule(id):
    dbConnection()
    data = (id,)
    cur.execute("select * from schedule where id = %s",data)
    rows = cur.fetchall()
    if cur.rowcount > 0:
        for row in rows:
            print("ID："+str(row[0]))
            print("日時："+str(row[2]))
            print("スケジュール："+str(row[1]))
            print()
    else:
        print("スケジュールが見つかりませんでした。")
    cur.close()
    conn.close()



print("スケジュール管理アプリケーションへようこそ。")
while True:
    print("**********メニュー**********")
    menu = input("1)スケジュール追加 2)スケジュール修正 3)スケジュール削除 4)スケジュール表示 9)終了：")

    if menu == '1':
        print("スケジュールに登録するデータを入力してください。")
        date = input("日付（年-月-日 時:分）：")
        note = input("スケジュール：")
        addSchedule(note,date)
    elif menu == '2':
        print("スケジュールを変更する内容を入力してください。")
        id = input("スケジュール番号：")
        date = input("日付（年-月-日 時:分）：")
        note = input("スケジュール：")
        updateSchedule(note,date,id)
    elif menu == '3':
        id = input("削除するスケジュールのIDを入力してください。:")
        deleteSchedule(id)
    elif menu == '4':
        displayMenu = input("1)全件表示 2)指定表示：")
        if displayMenu == '1':
            print()
            allShowSchedule()
        elif displayMenu == '2':
            id = input("スケジュールIDを指定してください。:")
            print()
            showSchedule(id)
    elif menu == '9':
        print("ありがとうございました。")
        break
    else:
        print("不正な値が入力されました。")
        continue