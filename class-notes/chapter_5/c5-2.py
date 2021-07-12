# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 10:31:34 2021

@author: user15
"""

# =============================================================================
# count = 1
# while count <= 5:
#     print(count)
#     count += 1
# =============================================================================

# =============================================================================
# from random import randint
# tickets = 5
# point = 0
# fmt = "{:>3}"
#
# while tickets > 0:
#     v = randint(1, 20)
#     print(fmt.format(v))
#     point += v
#     # tickets -= 1
#
# print("-" * 3)
# print(fmt.format(point))
# =============================================================================

# =============================================================================
# from random import randint
# count = 0
# while True:
#     a = randint(1, 13)
#     b = randint(1, 13)
#     c = randint(1, 13)
#     count += 1
#     if(a + b + c) == 21:
#         break
#
# print(a, b, c)
# print(count)
# =============================================================================
# =============================================================================
# # Pg115
# from random import randint
# miss = 0
# correct = 0
# print("問題！　3回間違えたら終了。　ｑ で止める")
# while miss < 3:
#     a = randint(1, 100)
#     b = randint(1, 100)
#
#     ans = a + b
#     question = f"{a} + {b} は? \n ==>"
#
#     value = input(question)
#
#     if value == "q":
#         break
#
#     if value == str(ans):
#         correct += 1
#         print("正解です！")
#
#     else:
#         miss += 1
#         print("間違い！", "x" * miss)
#         print("正解は：　",ans)
#
# print("-" * 20)
# print("正解：　", correct)
# print("間違い：　", miss)
#
# =============================================================================

# =============================================================================
# # Pg118
# 
# from random import randint
# numbers = []
# while len(numbers) < 10:
#     n = randint(0, 100)
#     if n in numbers:
#         continue
#     numbers.append(n)
# 
# print(numbers)
# 
# =============================================================================

# Pg 120
from random import randint

numbers = []
while len(numbers) < 10:
    n = randint(-10, 90)
    if n < 0:
        print("中断されました！")
        print(numbers, n)
        break
    if n in numbers:
        continue
    
    numbers.append(n)
else:
    print(numbers)









