# -*- coding: utf-8 -*-
"""
演習3
■ 仕様
数値を入力し、入力された数値の倍数を 300 まで表示するコンソールプログラムを作成してください。300 よりも
大きい数値は表示させません。 
■ 実行画面
数値を入力してください。:7 
0
7
14
21 ・・・ 287 294
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
