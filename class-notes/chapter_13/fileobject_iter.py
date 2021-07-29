# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 15:23:32 2021

@author: user24
"""

file = "./data/tsuretsuregusa.txt"

target = "心"

with open(file, "r", encoding="utf_8") as fileobj:
    while True:
        try:
            # use iterator to move through lines
            line = next(fileobj)
            # find returns the position of the target
            # -1 is False, can't find
            
            if line.find(target) >= 0:
                print(f"「{target}」が見つかりました。")
                # print the all the line
                print(line, end = "")
                break
        
        # next return error when can't find new line
        # raises error and break from loop
        except StopIteration:
            print(f"「{target}」は見つかりませんでした。")
            break
        
        





