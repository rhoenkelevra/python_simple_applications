# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 09:42:24 2021

@author: user15
"""
# =============================================================================
# s = "Apple iPhone と Google Android"
# print(s.upper())
# 
# print(s.lower())
# 
# print(s.swapcase())
# print(s)
# 
# s1 = "may the force be with you!"
# print(s1.capitalize())
# print(s1.title())
# =============================================================================


# =============================================================================
# # p87
# s1 ="どっどどどどどうど"
# print("count Do", s1.count("どど"))
# s = "apple pie"
# print("count p",s.count("p"))
# 
# print("count p up to 4th char:", s.count("p", 0 , 4))
# 
# print("find e",s.find("e"))
# print("find x",s.find("x"))
# print("reverse find e",s.rfind("e"))
# 
# s3 = "愛知県半田市"
# 
# ken_index = s3.find("県")
# 
# print(s3[:ken_index + 1])
# 
# s4 = 'employee'
# print(s4.replace("e", "x"))
# 
# print(s4.replace("e", "x", 2))
# 
# sj = "サクラ咲く"
# print(sj.replace("咲く", "舞う風"))
# 
# =============================================================================
t = "  Hello    \n"
print(t.strip())

t = 'abc .....'
print(t.rstrip("."))

t1 = '2, 3, 4,'
print(t1.rstrip(".,\n"))

t2 = "Hello World \n"
print(t2.rstrip(".,\n"))

t = "dog.peg.jp"
print(t.rstrip(".jpeg"))





