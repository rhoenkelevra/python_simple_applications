# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 11:29:52 2021

@author: user24
"""

def hello():
    print("ハロー")
    
msg = hello
msg()

def do(func):
    func()
    
def thanks():
    print("ありがとう")
    
def hi():
    print("やあ！")
    
condition = 2
if condition == 1:
    do(thanks)
else:
    do(hi)
    
    
# Pg 257
def calc(func, arg=1):
    price = func(arg)
    return price

def child(arg):
    return 400 * arg

def adult(arg):
    return 1200 * arg

age = 20
num = 3
if age < 16:
    price = calc(child, num)
else:
    price = calc(adult, num)
    
print(f"{age}歳、{num}人は{price}円です。")


#=============================================================================
# Pg 258
# 関数を作るため関数
# It is good for when we have to write a lof of similar functions 
# ie. remote controller, each button has a similiar function
# but are not equal
#　クロージャの定義
def charge(price):
    def calc(num):
        return price * num
    
    return calc

# クロージャ　（関数オブジェクト）　を２種類作る
child = charge(400) #  calc(num): ... 
adult = charge(1000) #  calc(num): ...

price1 = child(3)
price2 = adult(2)

print(price1)
print(price2)
#=============================================================================

#Pg 259
# 無名関数　ラムダ式
func = lambda w,h : w * h
num = func(3, 4)
print(num)
print(func(10, 10))


num = (lambda w, h : w * h)(4, 5)
print(num)

price = lambda burger=1, potato=0: burger*240 + potato*100
print(price(potato = 2))

# Pg 260 sort()
def size(item):
    sizelist = ["XS", "S", "M", "L"]
    pos = sizelist.index(item)
    return pos

data = ["S", "M", "XS", "L", "M", "M", "XS", "S", "M", "L", "M"]
data.sort(key = size)
print(data)

sizelist = ["XS", "S", "M", "L"]
data.sort(key = lambda item: sizelist.index(item)) 
# can't use print(data.... ) because sort returns a new list? 
# it's printing None
print(data)


'''
The value of the key parameter should be a function (or other callable) that takes a single argument and returns a key to use for sorting purposes. This technique is fast because the key function is called exactly once for each input record.

'''

# Pg262 map()

nums = [4, 3, 7, 6, 2, 1]
nums2 = list(map(lambda x: x * 2, nums))
print(nums2)

# filter()
nums = [4, -2, 9, 1, -2, -4, 5]
nums2 = list(filter(lambda x : x>0, nums))
print(nums2)

    
    
    
    
    
    
    
    
    