# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 09:33:36 2021

@author: user15
"""

s = '出席番号1番の山田が5分間スピーチを行わせていただきます。私の気になるITニュースについてお話しさせていただきます。よろしくお願いいたします。〜中略〜データとして4月は100人、5月は150人とひと月で大きく成長しています。'




# ① 発表者の出席番号は何番か出力せよ（出席番号は上記文字列から抜き出すこと）
print('出席番号:',s[4 : 4 + 2])


# ② 発表者の名前を下記のように出力せよ（名前は上記文字列から抜き出すこと）
print('発表者：',s[7 : 7 + 2])
#	発表者：〇〇


#③ スピーチのテーマを下記のように出力せよ（スピーチのテーマは上記文字列から抜き出すこと）
# print(len(s))
print('今日のテーマ：', "「",s[31 : 31 + 10],"」")
print(f"今日のテーマ：「{s[31:41]}」")
# 	今日のテーマ：「〇〇」


#④ データ部分の4月と5月の人数を足し合わせ下記のように出力せよ（計算に使用する数値は上記文字列から抜き出すこと）
d1 = s[84:87]
d2 = s[92:95]
print('人数合計：',int(d1) + int(d2))
print(f"Ninzu {int(d1) + int(d2)}人")

#	人数合計：〇〇人





