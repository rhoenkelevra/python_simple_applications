# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 12:01:23 2021

@author: user24
"""

# =============================================================================
#
# Open file and reads it  
#
# file = './data/fox.txt'
# fileobj = open(file)
# text = fileobj.read()
# fileobj.close()
# print(text)
# 
# =============================================================================

# # Pg 304

# Open file with .. don't need to close after 

# file = './data/fox.txt'
# with open(file) as fileobj:
#     text = fileobj.read()
#     print(text)
    

file = './data/fox.txt'
with open(file) as fileobj:
    text = fileobj.read()
    newtext = text.rstrip(".")
    wordlist = newtext.split(" ")
    print(wordlist)






