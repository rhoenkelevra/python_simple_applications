# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 09:44:01 2021

@author: user24
"""

# Pg320　グラフを描く

# import matplotlib.pyplot as plt

# price = [200, 300, 400, 500, 600]

# count = [31, 29, 25, 28 , 26]

# plt.plot(price, count)
# plt.tite("count - price")
# plt.xlabel("price")
# plt.ylabel("count")

# plt.show()

# # ==========================================================================

# # グリードとマーカーを表示する

# import matplotlib.pyplot as plt

# price = [200, 300, 400, 500, 600]
# count = [31, 29, 25, 28 , 26]

# plt.plot(price, count, marker="o")
# plt.title("count - price")
# plt.xlabel("price")
# plt.ylabel("count")
# plt.grid(True)
# plt.show()


# # ==========================================================================
# # Pg322 - グラフを画像保存する
# import matplotlib.pyplot as plt
# import math

# X = range(0, 360)
# Y = [math.sin(math.radians(d)) for d in X]
# plt.plot(X, Y)
# plt.savefig("sin.png")
# plt.show()


# # ==========================================================================
# # Pg323 複数のグラフを重ねる
# import matplotlib.pyplot as plt
# import math

# X = range(0, 360)
# S = [math.sin(math.radians(d)) for d in X]
# C = [math.cos(math.radians(d)) for d in X]
# plt.plot(X, S)
# plt.plot(X, C)
# plt.show()

# # =============================================================================

# # Pg 324

# import matplotlib.pyplot as plt

# X = [100, 200, 300, 400, 500]
# Y1 = [40, 65, 80, 100, 90]
# Y2 = [34, 56,75,91,79]
# Y3 = [25, 47, 68,76,73]
# Y4 = [15, 40, 52, 64, 69]

# plt.plot(X, Y1, marker="o", color="blue", linestyle="-")
# plt.plot(X, Y2, marker="v", color="red", linestyle="--")
# plt.plot(X, Y3, marker="^", color="green", linestyle="-.")
# plt.plot(X, Y4, marker="d", color="m", linestyle=":")

# plt.savefig("colors.png")
# plt.show()

# ==========================================================================

# Pg. 325 凡例を付ける
import matplotlib.pyplot as plt

X = [100, 200, 300, 400, 500]
Y1 = [40, 65, 80, 100, 90]
Y2 = [34, 56,75,91,79]
Y3 = [25, 47, 68,76,73]

plt.plot(X, Y1, marker="o", color="blue", linestyle="-", label="Y1")
plt.plot(X, Y2, marker="v", color="red", linestyle="--", label="Y2")
plt.plot(X, Y3, marker="^", color="green", linestyle="-.", label="Y3")

plt.legend(loc = "upper left")
plt.show()

