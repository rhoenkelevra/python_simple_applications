# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 09:30:04 2021

@author: user24
"""
# pythonのファイルを２つ作成し、プログラムを完成させなさい。


# 【calc.py	加算、減算、乗算、除算の4つの関数を持つモジュール】

# 	①	add関数	引数を２つ受け取り加算の結果を戻り値として返す

# 	②	sub関数	引数を２つ受け取り減算の結果を戻り値として返す

# 	③	mul関数	引数を２つ受け取り乗算の結果を戻り値として返す

# 	④	div関数	引数を２つ受け取り除算の結果を戻り値として返す



# 【renshu11.py	「calc.py」モジュールを使用し計算を行う実行プログラム】

# 	①	「calculation.py」を読み込む

# 	②	利用者から数値を２つ受取る

# 	③	数値変換を行う

# 	④	4つの関数を発動し戻り値を受取る

# 	⑤	「◯算の結果は：△」の形で関数の数分出力する

from calc import add, subtract, multiply, divide


while True:

    num1 = input("一つ目の数値を入れてください  \n-->")
    num2 = input("二つ目の数値を入れてください  \n-->")

    try:
        num1 = int(num1)
        num2 = int(num2)
    except:
        print("数値を入れてください。")
        continue

    addResult = add(num1, num2)
    subResult = subtract(num1, num2)
    mulResult = multiply(num1, num2)
    divResult = divide(num1, num2)

    results = {
        "加算": addResult,
        "減算": subResult,
        "乗算": mulResult,
        "除算": divResult,
    }

    for key in results:
        value = results[key]
        print(f"{key}の結果は：　{value}")

    break




