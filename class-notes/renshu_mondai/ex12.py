import mysql.connector as mydb 
import matplotlib.pyplot as plt

conn = mydb.connect(
        host = "localhost",
        port = "3306",
        user = "rhoen",
        password = "pass",
        database = 'ex'
       
    )
cur = conn.cursor(buffered=True)

def pull(id):
    
    cur.execute("select japanese, math, science, socialstudies, english from test_average where id=%s", (id,))
    rows = cur.fetchall()
    entries = []
    for entry in rows:
        entries.append(entry)
    return entries

X = ["J", "M", "S", "SS", "E"]
labels = X
Y1 = pull(1)
print(Y1)
Y2 = pull(2)
print(Y2)

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)

ax1.bar(X, Y1[0], color='b') # 
ax1.set_title("A 組")

ax2 = fig.add_subplot(1, 2, 2)
ax2.bar(X, Y2[0], color='b')
ax2.set_title("B 組")

plt.show()
cur.close()
conn.close()