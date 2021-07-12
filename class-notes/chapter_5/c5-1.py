# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 11:45:14 2021

@author: user15
"""
# =============================================================================
# pg 98
# v = -1
# if v < 0:
#     v = 8
#
# v = v * 2
# print(v)
#
# v = 3
# if v < 0:
#     v = 0
#
# v = v * 2
# print(v)
#
# v = -1
# if v < 0:
#    v = 0
# v = v * 2
# print(v)
# =============================================================================
# =============================================================================
# # pg100
# sum = 50 + 37 + 10
# limit = 100
# if sum >= limit:
#     result = "合格"
# else:
#     result = '不合格'
#     result += "／" + str(sum - limit)
#
# print(sum)
# print("-" * 20)
# print(result)
# print(sum, "-" * 20, result, sep="\n")
#
# =============================================================================
# =============================================================================
# 
# #  Pg102
# from random import randint
# point = randint(0, 100)
# 
# if point >= 80:
#     result = 'A クラス'
# elif point >= 60:
#     result = 'B クラス'
# elif point >= 30:
#     result = 'C クラス'
# else:
#     result = "不適合"
# 
# print(f"{point}点：{result}")
# 
# =============================================================================

# =============================================================================
# # Pg104
# from random import randint
# size = randint(5, 20)
# weight = randint(20, 40)
# 
# if size >= 10:
#     if weight >= 25:
#         result = "合格"
#     else:
#         result = "不合格"
# else:
#     result = "不合格"
# 
# text = f"サイズ {size}、重量 {weight} ：{result}"
# print(text)
# =============================================================================

# =============================================================================
# # Pg 105
# from random import randint
# size = randint(5, 20)
# weight = randint(20, 40)
#  
# if (size >= 10) and (weight >= 25):
#     result = "合格"
# else:
#     result = "不合格"
# 
# text = f"サイズ {size}、　重量{weight}　： {result}"
# print(text)
# =============================================================================
# =============================================================================
# # Pg 106
# from random import randint 
# a = randint(0, 100)
# b = randint(0, 100)
# 
# if a >= 40 and b >= 40 and (a+b) >= 120:
#     result = "合格"
# else:
#     result = "不合格"
# 
# text = f"a:{a}, b:{b}, 合計{a+b}: {result}"
# print(text)
# =============================================================================

# =============================================================================
# # Pg107
# from random import randint 
# size = randint(5, 20)
# weight = randint(20, 40)
# 
# if ()
# =============================================================================

# =============================================================================
# # Pg 108
# # not name => if name is empty is True
# name = ""
# if not name :
#     name = "rene"
#     
# print(name)
# 
# from random import randint
# num = randint(0, 100)
# # Joyo => sobra
# # 3 % 2 = 1 => True
# # num % 2 == 1
# if num % 2:
#     result = "奇数"
# # 4 % 2 = 0 => False    
# else:
#     result = "具数"
# 
# print(num, result)
# print(21%2)
# 
# =============================================================================

# Pg 110
from random import randint
a = randint(0, 100)
b = randint(0, 100)

if a>b:
    bigger = a
else:
    bigger = b
    
text = f"{a}と{b}では、 {bigger}が大きい。"
print(text)


bigger = a if a>b else b
text = f"{a}と{b}では、 {bigger}が大きい。"
print(text)

