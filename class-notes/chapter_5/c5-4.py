# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 14:45:50 2021

@author: user15
"""
# =============================================================================
# # Pg134
# while True:
#     num = input("何個ですか？　（ｑ）で終了 \n ==>")
#     if num == "q":
#         print("終了しました。")
#         break
#     
#     try:
#         price = 120 * int(num)
#         print("金額", price)
#     except:
#         print("エラーです。正しい数値を入れてください。")
# =============================================================================

# =============================================================================
# # Pg 135
# num = 0
# 
# try:
#     value = 120 / num
#     print(value)
# except:
#     print("エラーになりました。")
# finally:
#     print("計算終わり。")
#     
# 
# =============================================================================
# =============================================================================
# 
# # Pg 137, 138
# 
# sum = 7600
# while True:
#     num = input("何人ですか？　（ｑ　で終了）　\n ==>")
#     if num == "q":
#         print("終了しました。")
#         break
#     try:
#         price = round(sum / int(num))
#         if price < 0:
#             continue
#         print("1人当たりの金額：　", price)
#     
#     except ValueError:
#         print("数値を入れてください。")
#     except ZeroDivisionError:
#         print("0以外の数値を入れてください。")
#         
#         
#     # おすすめ　Always put a generic except so the system won't break
#     except:
#         print("そのほかのエラーです。")
# 
# 
# 
# =============================================================================

# Pg 140

sum2 = 7600
while True:
    num = input("何人ですか？　（ｑで終了） \n ==>")
    if num == "q":
        print("終了しました。")
        break
    try:
        price = round(sum2 / int(num))
    except Exception as error:
        print("エラーになりました。")
        print(error)
    else:
        if price < 0 :
            continue
        print("1人当たりの金額：　", price)














