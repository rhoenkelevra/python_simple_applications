import matplotlib.pyplot as plt
import mysql.connector as mydb
import numpy as np

conn = None
cur = None

#データベース接続
conn = mydb.connect(host="localhost",port="3306",user="user",password="pass",database="ex")
cur = conn.cursor()

#データベースからデータを取得
cur.execute("select * from nagoya_population")
rows = cur.fetchall()

#横軸の初期化
x = []
#縦軸の初期化
y_elderly = [] #elderly（高齢者）
y_young_old = [] #young_old（前期高齢者）
y_old_old = [] #old_old（後期高齢者）
 
for row in rows:
    x.append(int(row[1])) #year（年）
    y_elderly.append(int(row[3])) #elderly（高齢者）
    y_young_old.append(int(row[4])) #young_old（前期高齢者）
    y_old_old.append(int(row[5])) #old_old（後期高齢者）
 
        
cur.close()
conn.close()


plt.plot(x,y_elderly,marker="o" )
plt.plot(x,y_young_old,marker="o" )
plt.plot(x,y_old_old,marker="o" )


plt.title("名古屋市の高齢者人口の推移",fontname="MS Gothic") #グラフタイトル
plt.xlabel("年",fontname="MS Gothic") #横軸ラベル
plt.ylabel("人口（人）",fontname="MS Gothic") #縦軸ラベル
plt.grid(True) #グリッドの表示
plt.legend(loc = "upper left") #凡例の位置
plt.legend(["高齢者", "前期高齢者","後期高齢者"] ,prop={"family":"MS Gothic"}) #凡例の表示
plt.xticks(np.arange(min(x), max(x)+1, 1.0)) #目盛間隔の設定

plt.show()

