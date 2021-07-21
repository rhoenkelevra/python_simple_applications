# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 10:50:00 2021

@author: user24
"""

# Pg291 
# Override

class Greet():
    def hello(self):
        print("やあ！")
        
    def bye(self):
        print("さよなら")
    
class Greet2(Greet):
    def hello(self, name = None):
        if name:
            print(name + "さん、　こんにちは。")
        else:
            super().hello()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        