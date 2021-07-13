# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 13:36:25 2021

@author: user15
"""

# Tuples
# Tuples are immutable
# Can't change after it's creation
# Don't have many built-in methods
# Are faster than list
# =============================================================================

a = (1, 2)
b = ("py", 3.6)
c = (89, 56, 75)
d = ((10, 20), (30, 40))
e = (3,)  # use comma to make the interpreter see as a tuple

# ( ) are opcional
a = 1, 2
b = "py", 3.6
c = 89, 56, 75
d = (10, 20), (30, 40)
print(a, b, c, d)
print(type(a))

for n in d:
    for y in n:
        print(y)

x = 10, 20
y = 30, 40
z = x + y
print(z)

numbers = (1, 2, 3, 55, 44, 33)

# =============================================================================
param = int(input("enter id"))

for n in number:
    if n == param:
        print("aru")

# =============================================================================

# Pg 186
data = tuple(range(-5, 6))
print(data)

week = tuple("月火水木金土日")
print(week)

color = ["blue", "black", "green"]
data = tuple(color)
print(data)

data = ('blue', 'black', 'green')
data_list = list(data)
print(data_list)

color = ("green", "red", "blue", "yellow")
print(color[0])
print(color[1])
print(color[-1])

for item in enumerate(color, 1):
    print(item)

for item in numbers:
    print(item * item)

## Tuple Unpacking
# ## From the tuple assign variables
# ## like javasript
#
(a, b) = (100, 200,)
print(a)
print(b)
print(a, b)
print((a,b))
print(type(a))
print(type((a, b)))
a = a + b
print(a)

data = (12, 15)
(boy, girl) = data
all = boy + girl
print(boy, girl, all)
print(type(data))
print(type(boy))
print(type(all))

# =============================================================================

x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]

zip_obj = zip(x, y, z) # creates a zip obj
print(type(zip_obj)) # display obj class zip
xyz = list(zip_obj) # turn it into list
print(xyz)
