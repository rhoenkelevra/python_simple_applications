# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 11:34:28 2021

@author: user15
"""
# =============================================================================
# # Pg 142
# numbers = [4, 8, 15, 16, 23, 42]
# colorss = ['red', 'green', 'blue']
# print(numbers)
# print(colorss)
#
# =============================================================================
# =============================================================================
# #  Pg 144
# num = [0] * 10
# print(num)
#
# strs = ["xy"] * 5
# print(strs)
#
# result = [False] * 5
# print(result)
#
# data = [1, 2, 3]
# print(data * 5)
# =============================================================================
# =============================================================================
#
# # Pg145
#
# thelist = list(range(-5, 6))
# print(thelist)
#
# evenlist = list(range(0, 10 ,2))
# print(evenlist)
#
# oddlist = list(range(1, 10, 2))
# print(oddlist)
#
# list_x3 = list(range(0, 20, 3))
# print(list_x3)
#
# list_happy = list("happy")
# print(list_happy)
# list_happy.join("-")
# print(list(list_happy))
#
# week = list("月火水木金土日")
# print(week)
#
# =============================================================================

# =============================================================================
# # Pg 145
#
# colors = ["blue", "red", "green", "yellow"]
# print(colors[0])
# print(colors[1])
# print(colors[2])
# print(colors[3])
# print(colors[-1])
# print(colors[-2])
#
# colors[2] = "black"
# print(colors)
#
# =============================================================================
# =============================================================================
#
# # Pg 147
# list_a = [["apple", "peach", "beach"], ["cabbage", "carrot", "potato"]]
# list_b = [
#     [
#         ["p", "y"], ["t", "h"]
#     ],
#     [
#         ["o", "n"], ["3", "note"]
#     ]
# ]
#
# print(list_a[1][0])
# print(list_b[0])
# print(list_b[0][0])
# print(list_b[0][0][0])
# print(list_b[1][1][1])
#
# =============================================================================
# =============================================================================
#
# r101 = 'saito'
# r201 = 'aoki'
#
# floor1 = [r101]
# floor2 = [r201]
# apartment = [floor1, floor2]
#
# # Don't work
# # print(apartment.floor1.r101)
#
#
# =============================================================================
# =============================================================================
# # Pg 149
# pos = int(input("取り出す位置：　\n ==>"))
# colors = ["blue", "red", "green", "yellow"]
# length = len(colors)
# if -length <= pos < length:
#     item = colors[pos]
#     print(item)
# else:
#     print("エラーになりました。")
#
# =============================================================================

# =============================================================================
#

# pos = int(input("取り出す位置：　\n ==>"))
# colors = ["blue", "red", "green", "yellow"]
# try:
#     item = colors[pos]
#     print(item)
# except IndexError:
#     print("Index Error")
# except Exception as error:
#     print(error)
#
# =============================================================================

# =============================================================================
# # Pg 151
# data = []
# data.append(10)
# data.append(20)
# print(data)
#
# data.append(30)
# print(data)
#
# =============================================================================
# =============================================================================
# 
# # Pg 152, 153
# 
# # data = ['a', 'b', 'c', 'd', 'e', 'f']
# # data.insert(3, 'new')
# # print(data)
# 
# fruits = ["apple", "orange", "banana", "peach"]
# # dessert = fruits.pop()
# # print(dessert, "\n", fruits)
# 
# # # Specific position
# # dessert = fruits.pop(0)
# 
# if  fruits: #if the list is empty returns False
#     dessert = fruits.pop() 
#     print("デザートは" + dessert)
# print(fruits)
# 
# 
# 
# =============================================================================
# =============================================================================
# 
# # Pg 154
# fruits = []
# try:
#     dessert = fruits.pop()
#     print("Dessert is ", dessert)
#     print(fruits)
# except:
#     print("Error")
# 
# =============================================================================
# =============================================================================
# 
# colors = ['blue', 'red', 'yellow', 'red', 'green']
# print('削除前', colors)
# target = 'red'
# 
# # removes only the first instance of the target value
# if target in colors :
#     colors.remove(target)
# print("削除後", colors)
# 
# Remove all instances of the target value 
# 
# while target in colors:
#     colors.remove(target)
# print("削除後", colors)
# 
# =============================================================================

# =============================================================================
# # Pg 156
# message = "may the force be with you !"
# without param will separete each word
# with a param, will give a list with the string as value
# words = message.split()
# print(words)
# 
# =============================================================================

# =============================================================================
# # Pg 157
# fruits = "apple, orange, banana, mango"
# # ",space" will separate and remove the spaces
# fruit_list = fruits.split(", ")
# print(fruit_list)
# 
# colors = "red,blue,  green, white  ,  black"
# colors = colors.replace(" ", "")
# color_list = colors.split(",")
# print(color_list)
# 
# =============================================================================
# Pg 158

result = "23,45,56,87,90,123,231,256,321"
result_list = result.split(",", 3)
print(result_list)

top3 = result.split(",", 3)[:3]
print(top3)

members = ["Tom", "Jerry", "Spike"]
name = " and ".join(members)
print(name)














