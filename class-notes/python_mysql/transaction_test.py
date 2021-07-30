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

try:
    #　登録済みを確認
    isbn = input("ＩＳＢＮ　を入れてください：　\n--> ")
    cur.execute("select * from books where isbn = %s", (isbn,))
    cur.fetchall()
    #書籍登録済みを判定
    
    if cur.rowcount > 0:
        print("torokuzumi")
        exit(0)
    else:
        # mitorokunobai
        title = input("Insert title")
        price = input("Insert price")
        publish = input("Insert publisher")
        publishDate = input("date published yyyy-mm-dd")
        categoryId = input("insert category")
        authorId = input("insert author id")
        
        cur.execute("select * from author where author_id=%s", (authorId,))
        cur.fetchall()
        
        if cur.rowcount == 0:
            authorflg = True
            name = input("insert author name")
            nameKana = input("insert author kana")
    
        cur.execute("select * from category where category_id = %s", (categoryId,))
        cur.fetchall()
        
        if cur.rowcount == 0:
            categoryflg = True
            categoryName = input("insert category name")
    
        if categoryflg:
            cur.execute("insert into category values(%s, %s)", (categoryId, categoryName))
            if cur.rowcount == 0:
                raise Exception
                
        if authorflg:
            cur.execute("insert into author values(%s, %s, %s)", (authorId, name, nameKana))
            if cur.rowcount == 0:
                raise Exception
                
        data = (isbn, title, price, publish, publishDate, categoryId)
        cur.execute("insert into books values(%s,%s,%s,%s,%s,%s)", data)
        print("7")
        if cur.rowcount == 0:
            raise Exception
            
        cur.execute("insert into author_books values(%s,%s)", (isbn, authorId))
        if cur.rowcount == 0:
            raise Exception
        
        conn.commit()
        print("toroku shimashita")
        
except:
    conn.rollback()
    print("failed")
    
# カーソルとコネクションを切断
cur.close()
conn.close()  
    
    