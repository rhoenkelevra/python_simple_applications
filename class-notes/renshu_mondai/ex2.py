# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 14:12:24 2021

@author: user24
"""
# countとtotalの変数を初期化する
count = 0
total = 0

# 切り替えるためループ
while True:
    # ユーザからインプット数値
    ans = input("数値を入れてください。　(End 終了)\n--> ")
    
    # Ｅｎｄインプットなら終了
    if ans == 'End':
        break
    
    # インプットを整数にする
    ans = int(ans)
    
    # インプット変数＋１
    count += 1
    #インプット値をＴＯＴＡＬに追加する
    total += ans
    
# 回数と合計をプリントする
print(f"{count}回入力しました。")
print(f"合計は{total}です。")
    
    
    
    