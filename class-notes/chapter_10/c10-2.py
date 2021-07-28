# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 14:39:01 2021

@author: user24
"""

# Pg240
# キーワード引数 Named Parameters
def price(adult, child):
    return(adult * 1200) + (child * 500)


print(price(adult = 1, child = 2))

# # ==========================================================================
# Pg244
# 初期値がある引数 Default parameters
# Best practice, is to leave the default parameters for last
# because the order of the parameters are important

def calc(size, num = 6):
    unit_price = {"S": 120, "M": 150, "L": 180}
    price = unit_price[size] * num
    return(size, num, price)

a = calc("S", 2)
print(f"{a[0]}サイズ、{a[1]}個、{a[2]}円")

b = calc("M")
print(f"{b[0]}サイズ、{b[1]}個、{b[2]}円")

# # ===========================================================================
# Pg245
# キーワード引数を利用して特定の引数だけ指定する

def calc(size = "M", num = 6):
    unit_price = {"S": 120, "M": 150, "L": 180}
    price = unit_price[size] * num
    return(size, num, price)

a = calc()
print(f"{a[0]}サイズ、{a[1]}個、{a[2]}円")

b = calc("L")
print(f"{b[0]}サイズ、{b[1]}個、{b[2]}円")

c = calc(num = 1)
print(f"{c[0]}サイズ、{c[1]}個、{c[2]}円")

#===========================================================================
# 7/19
# Pg246


# User *args when we don't know the exact number of args the function needs
# the args can be any name, the important is the *
# * tells python to unpack the arguments
def fruit(*args):
    print(args)

fruit("apple", "orange", "ichigo", "banana")

def route(start, end, *args):
    route_list = [start]
    route_list += list(args)
    route_list += [end]
    
    route_str = "->".join(route_list)
    print(route_str)
    
start = "東京"
end = "宮崎"
    
route(start, end, "神戸","長崎", "熊本")
    
# **kwargs
# like *args, but get the args as dictionary

def fruit(**kwargs):
    print(kwargs)
    
fruit(apple=2, orange=3, banana=1)


def entry(name, gender, **kwargs):
    data = {'name': name, 'gender': gender}
    data.update(kwargs)
    print(data)
    
# with named args 
entry(name = '大山 板道',gender = '男性', age=27, course="E")
# name and gender are already specified inside the function, so don't need the 
# named args 
entry('大山 板道', '男性', age=27, course="E")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    