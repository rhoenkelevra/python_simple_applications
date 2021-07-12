# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 15:07:50 2021

@author: user15
"""

a = [1, 2, 2, 2, 3, 4, 10]
b = [2, 10]

for i in a:
    for j in b:
        if j == i:
            a.remove(i)

print(a)
