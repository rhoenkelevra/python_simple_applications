# hukushu0706

s = "出席番号1番の山田が5分間スピーチを行わせていただきます。私の気になるITニュースについてお話しさせていただきます。よろしくお願いいたします。?中略?データとして4月は100人、5月は150人とひと月で大きく成長しています。"

# �@ 発表者の出席番号は何番か出力せよ（出席番号は上記文字列から抜き出すこと）

print(s[4 : 4 + 2])

# �A 発表者の名前を下記のように出力せよ（名前は上記文字列から抜き出すこと）
# 	発表者：〇〇

print("発表者：" + s[7 : 7 + 2])

# �B スピーチのテーマを下記のように出力せよ（スピーチのテーマは上記文字列から抜き出すこと）
# 	今日のテーマ：「〇〇」

print("今日のテーマ：「" + s[31 : 31 + 10] + "」")


# �C データ部分の4月と5月の人数を足し合わせ下記のように出力せよ（計算に使用する数値は上記文字列から抜き出すこと）
# 	人数合計：〇〇人

print("人数合計：" + str(int(s[84 : 84 + 3]) + int(s[92 : 92 + 3])) + "人")
