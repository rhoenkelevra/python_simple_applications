import mysql.connector as mydb

conn = mydb.connect(
    host="localhost",
    port="3306",
    user="rhoen",
    password="pass",
    database="book"
)
cur = conn.cursor()

query = "select * from author where author_id = %s " # '%s' did't work

# "select * from author where author_id = '" + id + "'"
# this is valid, but it is vulnerable against SQL Injections
# ' 'x' = 'x -> returns true, so the code will run

while True:
    id = input("author_id を入れてください\n--> ")

    data = (id,)
    if id == "q":
        break
    
    cur.execute(query, data) # the second param must be a tuple 
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    if id in rows:
        for row in rows:
            print(row)
    else:
        print("未登録です。")

   
print(cur.rowcount, "件、取得しました")


cur.close()
conn.close()

#  