# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 09:32:26 2021

@author: user24
"""

class InputSave():
    def __init__(self, input_save):
        self.__input_save = input_save
        
    @property
    def input_save(self):
        return f"入力したデータは：{self.__input_save}です。"
        
    
    
    
    