# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 13:31:06 2021

@author: user24
"""

'''
Suchi wo nyuryoku
only accepts integer
end shuryou
creates a graph as image
'''


import matplotlib.pyplot as plt
cnt = 0
Y = []
while True:
    ans = input("数値を入力してください \n-->")
    if ans == "end":
        break

    try:
        ans_int = int(ans)
        Y.append(ans_int)
        cnt += 1
    except:
        print("文字列を読めない！数値を入れてください。")
    except Exception as error:
        print(error)

X = range(0, cnt)
plt.plot(X, Y, marker="o", color="r", linestyle="--")
plt.savefig("test.png")
# plt.xlabel("入力順番") # Japanese char return erro
plt.show()


# ==========================================================================

'''

'''