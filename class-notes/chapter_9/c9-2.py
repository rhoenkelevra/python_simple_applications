# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 09:31:01 2021

@author: user15
"""
# =============================================================================
# colors = {"1": "blue", "2": "red"}
# print(colors["1"])
# # if key don't exist returns "KeyError"
#    
# 
# 
# # city = input("調べる地区名: ")
# members = {"東京": 21, "大阪": 15, "福岡": 11}
# # try:
# #     value = members[city]
# #     print(f"{city}の値は{value}です。")
# # except KeyError:
# #     print(f"{city}のデータはありません。")
# # except Exception as error:
# #     print(error)
#     
# print(members.get("京都"))
# # if key don't exist returns None
# 
# ## Find if key exists
# user = dict.fromkeys(["id", "name", "age"], 0)
# print("age" in user)
# 
# # key is a keyword 
# fruit = {"apple": 7, "orange": 5, "mango": 3, "peach": 6}
# for key in fruit:
#     value = fruit[key]
#     print(f"{key}が{value}個")
#     
# 
# # GET keys to list
# # fruit.keys()
# keys = list(fruit.keys())
# print(keys)
# 
# keys = [key.capitalize() for key in fruit.keys()]
# print(keys)
# 
# # GET values to list
# # fruit.values()
# values = list(fruit.values())
# print(values)
# 
# print(sum(fruit.values()))
# 
# # GET key/value pairs
# # fruit.items()
# fruitsDictList = list(fruit.items())
# print(fruitsDictList)
# 
# for key, value in fruit.items():
#     print(f"{key}が{value}個。")
#     
#     
# =============================================================================

# =============================================================================
# # Pg227
# fruit = {"apple": 7, "orange": 5, "mango": 3, "peach": 6}
# 
# while fruit:
#     key = input("どのフルーツを取り出しますか？　（ｑで終了）")
#     if key == "":
#         continue
#     if key == "q":
#         print("終了しました。")
#         break
#     
#     
#     
#     try:
    ## !! TODO erase one count at time 
#         fruitcount = fruit[key]
#         fruitcount -= 1
#         # if fruitcount == 0:
#         #     value = fruit.pop(key)
#         #     print(f"no more {key}")
#         # value = fruit.pop(key)
#         print(f"{key}は{fruitcount}個")
#         
#         
#     except KeyError:
#         print(f"{key}はありません。")
# 
#     except Exception as error:
#         print(error)
#         break
# else:
#     print("もう空っぽです。")
#     
# =============================================================================
# Pg 229

# popitem() pop a random item from dict
fruit = {"apple": 7, "orange": 5, "mango": 3, "peach": 6}
while fruit:
    ans = input("フルーツを取り出しますか？　（ｙ/ｎ）：")
    if ans == "y":
        key, value = fruit.popitem()
        print(f"{key}は{value}個")
    elif ans == "n":
        print("終了しました。")
        break
else:
    print("もう空っぽです。")