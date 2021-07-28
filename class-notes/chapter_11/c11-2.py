# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 14:17:26 2021

@author: user24
"""

colors = ['red', 'blue', 'green', 'yellow']
colors_iter = iter(colors)

print(type(colors_iter))

print(next(colors_iter))
print(next(colors_iter))
print(next(colors_iter))
print(next(colors_iter))
print(next(colors_iter)) # end of list: StopIteration error
















































