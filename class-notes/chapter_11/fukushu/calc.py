# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 09:29:53 2021

@author: user24
"""

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        res = num1 / num2
        return res
        
    except ZeroDivisionError as error:
        print("0 で除算できません")
        return error
