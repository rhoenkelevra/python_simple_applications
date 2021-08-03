# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import mysql.connector as mydb 
import matplotlib.font_manager as font_manager
font = font_manager.FontProperties(fname='C:/WINDOWS/Fonts/MS GOTHIC.TTC')


# =============================================================================
#                                    コネクション
# =============================================================================
conn = mydb.connect(
        host = "localhost",
        port = "3306",
        user = "rhoen",
        password = "pass",
        database = 'nagoya_pop'
       
    )
cur = conn.cursor(buffered=True)
# =============================================================================

def pull(col):
    
    cur.execute(f"select {col} from nagoya_population")
    rows = cur.fetchall()
    entries = []
    for entry in rows:
        entry_y, = entry
        entries.append(entry_y)
    return entries

year = 'year'
elderly = 'elderly'
young_old = 'young_old'
old_old = 'old_old'

year_x = pull(year)
elderly_y = pull(elderly)
young_old_y = pull(young_old)
old_old_y = pull(old_old)


plt.plot(year_x, elderly_y, marker="o", color="blue", linestyle="-", label="高齢者")
plt.plot(year_x, young_old_y, marker="^", color="orange", linestyle="-.", label="前期高齢者")
plt.plot(year_x, old_old_y, marker="d", color="green", linestyle=":", label="後期高齢者")

plt.title("名古屋市の高齢者人口", fontname="MS Gothic")
plt.xlabel("年", fontname="MS Gothic")
plt.ylabel("人口", fontname="MS Gothic")
plt.legend(loc = "upper left", prop={"family": "MS Gothic"})

plt.savefig("test.png")
plt.show()

cur.close()
conn.close()
    
