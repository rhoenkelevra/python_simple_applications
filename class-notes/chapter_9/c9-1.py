# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 13:47:35 2021

@author: user15
"""

# 辞書
from random import randint
stock = {
    "S": 7,
    "M": 12,
    "L": 3
}
result = {"t1": True, "t2": False, "t3": True}
point = {10: 5.37, 20: 5.56, 30: 5.05, 40: 5.16}

print(stock.get("S"))

obj = {
    "values": {
        "one": 1,
        "two": 2
    }
}
# getting nested dict values
print(obj.get("values").get("one"))

# The key is immutable
# so we can use tuples as key
d = {(2011, "ab"): 10, (2011, "ax"): 12.5, (2013, "bw"): 16}

len(stock)
# List of Tuple (key, value) to dict
data = dict([("yellow", 3), ("blue", 6), ("green", 5)])
print(data)

# key, value from list to dict using zip
keys = ["yellow", "blue", "green"]
values = [3, 6, 5]
data = dict(zip(keys, values))

# Tuple of list to dict
data = dict((["yellow", 3], ["blue", 6], ["green", 5]))
print(data)

# List of list to dict
data = dict([["blue", 1], ["red", 2], ["white", 3]])
print(data)


data = dict(yellow=3, blue=6, green=5)
print(data)

data = ["name", "email", "phone"]
stock = dict.fromkeys(data, "")
print(stock)

stock2 = dict.fromkeys("SML", 0)
# if second arg is not provided, default is NONE
print(stock2)

data = {"yellow": 3, "blue": 6, "green": 5}
data["blue"] = 10
data["white"] = 5
print(data)


data = {"yellow": 3, "blue": 6, "green": 5}
data.setdefault("blue", 10)
data.setdefault("white", 10)
# print(data)

# Pg 219
# update
data = {"a": 10, "b": 20, "c": 30}
newdata = {"a": 15, "d": 99}
data.update(newdata)

# Pg 220
# delete
fruit = {"apple": 7, "orange": 5, "mango": 3}
del fruit["mango"]

fruit.clear()

# Dictionary Comprehension
# dictionary = {key: value for vars in iterable}

keys = ["green", "red", "blue", "yellow"]
data = {key: randint(1, 100) for key in keys}
print(data)

unicode = {letter: ord(letter) for letter in "hello"}
print(unicode)

# passing values by reference
data = {"a": 100, "b": 200, "c": 300}
data_b = data
data_b["c"] = 0
print(data_b)
print(data)

# copying dict
data_c = data.copy()
data_c["c"] = 100
print(data_c)
