# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 09:54:36 2021

@author: user24
"""

total = 0
count = 0 
n_list = []
while True:
    ans = input("数値を入れてください。　（０で終了） \n-->  ")
    if ans == "0":
        break
    
    try:
        n_list.append(int(ans))
        total += int(ans)
        count += 1
        heiki = total / count
        
    except:
        print("エラー！！数値を入れてください")
        
print(f"合計は{total}です。")
print(f"平均は{heiki}です。")

total2 = sum(n_list)
heiki2 = total2 / len(n_list)
print(total2, heiki2)