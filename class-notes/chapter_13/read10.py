# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 14:43:44 2021

@author: user24
"""
# set the file path
file = './data/fox.txt'

# open file for reading only as fileobj
with open(file, "r", encoding = "utf_8") as fileobj:
    
    while True:
        # reads 10 letters
        text = fileobj.read(10)
        
        if text:
            # if there is something to read, print
            print(text)
        # if there is no more, break from while loop
        else: break






