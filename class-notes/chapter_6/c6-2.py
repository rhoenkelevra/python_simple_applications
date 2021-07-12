# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 15:33:12 2021

@author: user15
"""
""""
# Pg 159

abc = ["a", "b", "c"]
xyz = ["x", "y", "z"]

az = abc + xyz
print(az)

colors = []
colors += ["red"]
colors += ["white", "black"]
print(colors)

data = [1, 3, 5]
newdata = [2, 4, 6]
data.extend(newdata)
print(data)

# Pg 160
data2 = [1, 3, 5]
newData2 = [2, 4, 6]
data2.append(newData2)

print(data2)

colors = ["blue", "red", "green", "yellow", "pink", "black", "white"]
print(colors[:])  # print all
print(colors[3:])  # print from index 3
print(colors[:3])  # print up to index 3, not including it
print(colors[3:6])  # print from 3 to 6, not including 6

print(colors[-1:])  # print the last item
print(colors[-2:])  # print the last 2
print(colors[-2: -1])  # print the second last
print(colors[:-1])  # print all minus the last one

# Pg 161
# Slice
data = [10, 21, 35, 49, 51, 60, 77, 81, 92, 100]
n = 3  # 文割する位置
data1 = data[:n]  # get up to index 2
data2 = data[n:]  # from index 3
print(data1)
print(data2)

# Pg162
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[::2])  # jumps 1 from beggining up to the end
print(letters[1::2])  # jumps 1 from the second item

print(letters[1:5][::2])  # from i 2 -> 4 skip 1
print(letters[::2][1:5])
print(letters[1:5:2])  # from 1 to 4 skip 1

print(letters[::-1])  # get the list in reverse order
print(letters[::-2])  # get the list in reverse skipping one

print(letters[:-1][::-2])  # reverse from second last skip one

"""
"""
# Pg 162 リストを比較する

colors_a = ["green", "blue", "red"]
colors_b = ["green", "blue", "red"]
colors_c = ["green", "red", "blue"]

print(colors_a == colors_b)
print(colors_a == colors_c)

colors_d = colors_a
print(colors_a == colors_d)
colors_a.append("white")
print(colors_d)  # the values appended to a is also reflected on d

list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]
print(list_a is list_b)  # "is" is to compare the objects, not it's values
print(list_a is list_c)
print(list_a is not list_c)

list_a[0] = 99
print(list_a, list_b)  # changing one changes the other
list_b[1] = 100
print(list_a, list_b)  # both list changes

list1 = [10, 20, 30]
list2 = list1
list1 = [11, 22, 33] # this reassignment creates a new object
print(list1, list2) # list2 is still bounded to the original value of list1

"""
# Pg166
# For int and str if they refer to the same object
# "is" returns True
num_a = 10
num_b = num_a
print(num_a is num_b)

str_a = "こんにちは"
str_b = str_a
print(str_a is str_b)

# Pg 167 リストを複製する
list_mother = [10, 20, 30, 40, 50]
# copy the list to a new one, that don't point to the
list_work = list_mother.copy()
# same obj
print(list_work)  # has the same values as list_mother
print(list_mother is list_work)  # False, they don't point to the same obj

list_work[0] = 99
print(list_work)
print(list_mother)  # one changing doesn't affect the other

# using slice
list_father = [11, 22, 33, 44, 55]
list_child = list_father[:]
print(list_child)
print(list_child is list_father)  # False, they are not the same obj

# using list()
list_mother = [99, 88, 77, 66]
list_work = list(list_mother)
print(list_work)
print(list_work is list_mother)  # False
