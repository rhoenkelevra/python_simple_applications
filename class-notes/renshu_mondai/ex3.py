# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 14:20:03 2021

@author: user24
"""
# 変数を初期化する
total = 0

# ユーザからインプットをもらって整数にする
ans = int(input("数値を入れてください。"))
total += ans
# total変数が３００以下でしたらループに入る
while total < 300:
    # ループの値をプリント
    print(total)
    # total変数にans変数を足す
    total += ans
