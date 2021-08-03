import matplotlib.pyplot as plt
import mysql.connector as mydb
import numpy as np

onn = None
cur = None

#データベース接続
conn = mydb.connect(host="localhost",port="3306",user="user",password="pass",database="ex")
cur = conn.cursor()

#データベースからデータを取得
cur.execute("select * from test_average")
rows = cur.fetchall()

#列名取得リストの初期化
column = ["japanese","math","science","socialstudies","english"]

#横軸の初期化
x = [0,1,2,3,4] #教科のインデックス
#縦軸の初期化
y_a = [] #各教科の点数 A組
y_b = [] #各教科の点数 B組

#A組のデータ取得
for row in rows[0]:
    y_a.append(row) 

#B組のデータ取得
for row in rows[1]:
    y_b.append(row) 


print("行の取得")
print(y_a[2:])
y_a = y_a[2:]
y_b = y_b[2:]

 
cur.close()
conn.close()

fig = plt.figure() #図を作る

#1行2列の左
ax1 = fig.add_subplot(1,2,1)

ax1.bar(x,y_a,tick_label = column)
ax1.set_title("A組",fontname="MS Gothic")
ymin, ymax = plt.ylim() #現在のy軸のレンジを取得
ax1.set_ylim(0, 100) #A組のy軸の最小値と最大値

#1行2列の右
ax2 = fig.add_subplot(1,2,2)
ax2.bar(x,y_b,tick_label = column)
ax2.set_title("B組",fontname="MS Gothic")
plt.ylim(ymin,ymax) #y軸のレンジをax1と合わせる
ax2.set_ylim(0, 100) #B組のy軸の最小値と最大値

plt.show()

