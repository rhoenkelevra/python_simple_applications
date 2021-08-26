# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 10:24:34 2021

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
cur = conn.cursor()
ijoaiofja[jigf
        jfopaijfi[a
            jiafj[afj
                jioajf[
                    
try:
    #　登録済みを確認
    isbn = input("ＩＳＢＮ　を入れてください：　\n--> ")
    cur.execute("select * from books where isbn = %s", (isbn,))
    cur.fetchall()
    #書籍登録済みを判定
    
    if cur.rowcount > 0:
        print("登録済み")
        exit(0)
    else:
        # 未登録の場合
        title = input("タイトルを入れてください \n--> ")
        price = input("価額を入れてください \n--> ")
        publish = input("出版社を入れてください \n--> ")
        publishDate = input("出版日（yyyy-mm-dd型式）を入れてください \n--> ")
        categoryId = input("カテゴリーＩＤを入れてください \n--> ")
        authorId = input("著者IDを入れてください \n--> ")
        
        # Check if author is registered
        cur.execute("select * from author where author_id=%s", (authorId,))
        cur.fetchall()
        print("q1")
        # Create new author
        if cur.rowcount == 0:
            authorflg = True
            name = input("著者名を入れてください \n--> ")
            nameKana = input("著者名（カナを入れてください \n--> ")
            
        # Check if category is registered
        cur.execute("select * from category where category_id = %s", (categoryId,))
        cur.fetchall()
        print("q2")
        # Create new category
        if cur.rowcount == 0:
            categoryflg = True
            categoryName = input("カテゴリー名を入れてください \n--> ")
    
        if categoryflg:
            cur.execute("insert into category values(%s, %s)", (categoryId, categoryName))
            print("q3")
            if cur.rowcount == 0:
                print('e1')
                raise Exception
                
        if authorflg:
            cur.execute("insert into author values(%s, %s, %s)", (authorId, name, nameKana))
            print("q4")
            if cur.rowcount == 0:
                print('e2')
                raise Exception
                
        data = (isbn, title, price, publish, publishDate, categoryId)
        cur.execute("insert into books values(%s,%s,%s,%s,%s,%s)", data)
        print("q5")
        if cur.rowcount == 0:
            print('e3')
            raise Exception
            
        cur.execute("insert into author_books values(%s,%s)", (isbn, authorId))
        print("q6")
        if cur.rowcount == 0:
            print('e4')
            raise Exception
        
        conn.commit()
        print("登録しました。")
        
except:
    conn.rollback()
    print("登録に失敗しました。")
    
# カーソルとコネクションを切断
cur.close()
conn.close()  
    
    
