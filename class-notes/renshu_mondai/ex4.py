# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 14:33:25 2021

@author: user24
"""

# 変数初期化
filled = "■"
blank = "□"
#　カウンター変数（ループのカウントする為）
count = 0

#　０～６回ループする　（６行作る為）
for i in range(0, 6):
    #）０～１０回ループする（１０文字入れる為）
    for j in range(0, 10):
        #　どの文字入れる為カウンター変数で管理する
        # カウンターが偶数だったら黒
        if count % 2 == 0:
            print(filled, end="")
        #
        else:
            #奇数だったら白
            print(blank, end="")
        
    #　カウンター変数＋１
    count += 1    
    #　きれいにプリント為行入れる
    print("\n")