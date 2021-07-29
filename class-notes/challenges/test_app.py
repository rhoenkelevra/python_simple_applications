# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 13:12:25 2021

@author: user24
"""
# =============================================================================
# 
# import inspect
# from random import randint
#     
# def test(func):
#     argspec = inspect.signature(func)
#     func_len = len(argspec.parameters)
#     
#     print(f"function has {func_len} arguments")
#    
#     x = generateNumber(func_len)
#     z = func(x)
#     # print(x)
#     print(z)
# 
# def generateNumber(function_length):
#        func_arg_list = []
#        return func_arg_list
#    
# print(generateNumber(2))
# # test(compare)
# =============================================================================


import inspect
from random import randint

def kansu2(a, b):
    kazu = a + b
    return kazu

def test(func, r1, r2):
    x = 0
    sy = []
    a = len(inspect.signature(func).parameters)
    
    while x < a:
        sy.append(randint(r1, r2))
        x += 1
        
        if a == 4:
            kazu = func(sy[0], sy[1], sy[2], sy[3])
        if a == 2:
            kazu = func(sy[0], sy[1])
            
        return kazu
    
print(test(kansu2(1,1), 1, 10))