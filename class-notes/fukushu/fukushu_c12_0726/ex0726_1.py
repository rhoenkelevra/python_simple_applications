# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 09:27:43 2021

@author: user24
"""
total = 0 
while True:
    ans = input("数値を入れてください。　（０で終了） \n-->  ")
    
    try:
        ans = int(ans)
        if ans == 0:
            break
        total += ans
        
    except:
        print("エラー！！数値を入れてください")
        
print(f"合計は{total}です。")
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    