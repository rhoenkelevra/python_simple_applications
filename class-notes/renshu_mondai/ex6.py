# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 15:18:13 2021

@author: user24
"""

# カウンター変数を初期化する。カウンター変数はどのパターンにするか管理する
count = 0
# シャープ　と　ドットの変数
sharp = "#"
dot = "."

# ユーザから縦と横の値をもらって整数にする
tate = int(input("タテの値を入力してください。： "))
yoko = int(input("ヨコの値を入力してください。： "))

# 最初のループは行を作る、　行数は縦の変数
for l in range(0, tate):
    #　文字の値はyokoの変数です
    for i in range(0, yoko):
        # count の値によってパターンが変わる
        if count % 2 == 0: 
            #偶数の場合は＃。のパターンになる
            print(sharp + dot, end="")
        else:
            # 奇数の場合は　。＃
            print(dot + sharp, end="")
            
    # カウンター　＋１
    count += 1
    # きれいにプリントする為空行を入れる
    print("\n")
    