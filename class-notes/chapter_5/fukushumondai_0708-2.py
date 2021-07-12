# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 09:37:10 2021

@author: user15
"""

# =============================================================================
# キーボードから正の整数を 2 個入力し、入力データを加算した後、答えが 3 の倍数で偶数ならば解答を表示し、
# それ以外は「規格 外」と表示するフローチャートを書いてください。
# ※補足：複合条件を使用する事。数値判定は、不要とする。 
# =============================================================================


x = input("整数１を入力： \n ==>")
y = input("整数２を入力： \n ==>")

kaitou = int(x) + int(y)

# if not(kaitou % 3) and not(kaitou % 2):
#           0 => False      0 => False
#   not False => True        not False => True


# because is evaluating the result of kaitou % 3, if it is 0 
# than compare it to 0 
  
if (kaitou % 3 == 0) and (kaitou % 2 == 0):
    print(kaitou)
else:
    print("規格外")
    
    
