# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 10:27:16 2021

@author: user24
"""

# Pg327
import matplotlib.pyplot as plt
import numpy as np
from random import randint


labels = ["A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

x_pos = range(0, 10)
V = [91, 45, 17, 88, 47, 87, 49, 56, 67, 77]

# tick_label uses the label list
# if not specified will use the x_pos values
plt.bar(x_pos, V, tick_label=labels)
plt.show()

# Pg328 横棒グラフ

labels = ['A', 'B', 'C', 'D', 'E']
y_pos = range(0, 5)
V = [91, 45, 17, 88, 47]
plt.barh(y_pos, V, tick_label=labels)
plt.show()

#Pg329 積み上げ棒グラフ

labels = ['Green', 'Red', 'Yellow', 'Blue', 'Black', 'White']
x_pos = range(0, 6)
A = [34, 46, 54, 45, 56, 37]
B = [17, 47, 55, 67, 38, 49]

bar1 = plt.bar(x_pos, A, color='g')
bar2 = plt.bar(x_pos, B, color='c', bottom=A) # bottom=A means align with the A bar

plt.xticks(x_pos, labels, rotation='vertical') # X labels
plt.legend((bar1, bar2), ("man", "woman"), loc=1) # Legend -> loc accepts the code loc=1 or as string loc="upper right"
plt.show()


# Pg329, 330 散布図　サンプズ

def generateRandomList(ran_start, ran_final, range_start, range_final):
    return [randint(ran_start, ran_final) for num in range(range_start, range_final)]

# X = [randint(0, 100) for num in range(0, 20)]
# Y = [randint(0, 100) for num in range(0, 20)]
# plt.scatter(X, Y)
# plt.show()
# print(X, Y)


X1 = generateRandomList(0, 100, 0, 20)
Y1 = generateRandomList(0, 100, 0, 20)
X2 = generateRandomList(0, 100, 0, 20)
Y2 = generateRandomList(0, 100, 0, 20)

plt.scatter(X1, Y1, marker="+", color="r")
plt.scatter(X2, Y2, marker="^", color="g")
plt.show()


# Pg331 マーカーのサイズと透明度　トウメイド　transparency


# Pg334 円グラフ

labels = ['E', 'D', 'C', 'B', 'A']
# labels = ['A', 'B', 'C', 'D', 'E']

# !!! the values in the chart start from the last index because the list is inverted

# with the list in order, the chart is counter-clock
V = [17, 25, 47, 68, 91] #　値（反時計回り） the values are inverted
ex = [0, 0, 0.1, 0, 0] # パイの切り出し 

# to don't invert values, counterclock=False
plt.pie(V,
        explode=ex,  # the space between the slices
        labels=labels,
        autopct='%1.1f%%',  # format as % with one decimal point
        startangle=90,  # the angle that starts the display of data
        # counterclock=False
)    
plt.show()





