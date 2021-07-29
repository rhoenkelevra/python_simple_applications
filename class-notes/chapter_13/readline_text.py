# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 15:06:57 2021

@author: user24
"""

file = "./data/tsuretsuregusa.txt"
with open(file, "r", encoding="utf_8") as fileobj:
    while True:
        # set line as value of the file line
        line = fileobj.readline()
        # removes any white space at the end of string
        aline = line.rstrip()
        # if line exists, print line
        if aline:
            print(aline)
        # if don't exist, break from loop
        else:
            break




