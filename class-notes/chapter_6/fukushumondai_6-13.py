# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 09:32:12 2021

@author: user15
"""

# =============================================================================
# input Enter data 10x string
# menu 
# 1. nyuuryokujun -> user order, with numbers in front
# 2. shojun -> ascend order with numbers
# 3. koujun -> descen order
# 4. shuryo
# check for empty 
# 
# =============================================================================

itens = 0
data = []
while itens < 10: # TODO change number to 10
    
    item = input('データを入力してください。 \n -->')
    # if not itens:
        # continue
    if item:
        data.append(item)
        itens += 1
        

while True:
        
    display_data = input("1:入力順  2:昇順  3:降順 4: 終了  \n  -->")    
    if display_data == "4":
        break
    
    if display_data == "1":
        for i, str in enumerate(data, 1):
            print(f"{i}: {str}")
        
    if display_data == "2":
        data_asc = sorted(data)
        # for i, str in enumerat(sorted(data, 1, key = str.lower))
        for i, str in enumerate(data_asc, 1, key = str.lower):
            print(f"{i}: {str}")
        
    if display_data == "3":
        data_desc = sorted(data, reverse = True)
        for i, str in enumerate(data_desc, 1, key = str.lower):
            print(f"{i}: {str}")
        
