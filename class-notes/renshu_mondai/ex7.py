# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 15:28:43 2021

@author: user24
"""
'''
演習7
■ 仕様 
半径を入力し、入力された数値を元に「円の面積」、「円周」、「球の体積」、「球の表面積」を求めるコンソール
アプリケーションを作成してください。また、各数値を求めるメソッドを作成してください。 
■ 実行画面
半径を入力してください:7 
円の面積:153.94 -> area
円周:43.98 -> circumference
球の体積:1436.76  -> volume
球の表面積:615.75 -> surface area of sphere
'''
import math

# ユーザが半径を入力
r = int(input("半径を入力してください：　\n-> "))

# ＭＡＴＨ　モジュールからpiメッソド
pi = math.pi

# 円の面積のメソッド
def calc_area(r):
    a = pi * pow(r,2)
    print(f"円の面積:{a:.2f}")

# 円周のメソッド
def calc_circumference(r):
    c = (2 * pi) * r
    print(f"円周:{c:.2f}")

# 球の体積のメソッド
def calc_volume(r):
    v = (4/3  * pi) * pow(r, 3)
    print(f"球の体積:{v:.2f}")

# 球の表面積のメソッド
def calc_surface_area(r):
    s = (4 * pi) * pow(r,2)
    print(f"球の表面積:{s:.2f}")

# 　それぞれのメソッドを呼び出す。引数はユーザのインプット値ｓ
calc_area(r)
calc_circumference(r)
calc_volume(r)
calc_surface_area(r)