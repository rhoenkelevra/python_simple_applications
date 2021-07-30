# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 13:47:13 2021

@author: user24
"""
# 
# ユーザからインプット数値
ans = input("数値を入れてください。　(q 終了)\n--> ")

# インプットを整数にする
ans = int(ans)

# 数値割る２の残りは０でしたら　
if ans % 2 == 0:
    #偶数をプリント
    print("偶数です。")
    
else:
    #０ではないなら奇数をプリント
    print("奇数です。")