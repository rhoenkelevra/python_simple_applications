# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 11:52:27 2021

@author: user24
"""

class Person():
    def __init__(self, name):
        # __ means that the att is protected, can only be accessed and changed
        # by the class itself
        self.__name = name
        
    # This method can access and edit the protected __name    
    def who(self):
        print(self.__name + "です。")
        
# インスタンス生成　「インスタンスを作る」