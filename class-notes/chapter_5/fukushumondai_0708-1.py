# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 09:34:00 2021

@author: user15
"""

# =============================================================================
# キーボードからテストの点数を入力し、80 点以上ならば「合格」、80 点未満ならば「不合格」と表示するフローチャートを書いてくださ い。 
# ※補足：数値判定は、不要とする。（数字か文字かの判定を行う） 
# =============================================================================

x = input("テストの点数を記入して下さい。 \n ==>")
x = int(x)
if x >= 80:
    print(x, "合格")
else: 
    print(x, "不合格")