# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 15:00:04 2021

@author: user24
"""

# 変数
ball = "〇"

#　何個ボールを印刷する変数です
ball_cnt = 3
# カウンター変数
counter = 0

# 7行を印刷する為　
while counter <= 7 :
     # ボールかける　ボールカウンター変数を印刷するする　  
    print(ball * ball_cnt)
    # ボールカウンタを　ー＝１
    ball_cnt -= 1
    # 　カウンター変数　＋＝１
    counter +=1
    
    # ボールカウンタ０になったら
    if ball_cnt == 0:
        # 空行を含める
        counter += 1
        
        # ボールカウンター変数を３までループ
        while ball_cnt <= 3:
            # ボールかける　ボールカウンター変数を印刷するする　 
            print(ball * ball_cnt)
            # ボールカウンター変数をＵＰする
            ball_cnt += 1
            counter += 1
    