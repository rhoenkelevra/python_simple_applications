# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 15:24:11 2021

@author: user24
"""

# Pg290 
# Inheritance

from datalog import Datalog

class Mydata(Datalog):
    def printlog(self):
        for date, data in self.loglist:
            print(date, data)
            
            
            
obj = Mydata()
obj.log("abc")
obj.log("123")
obj.log("あいうえお")
obj.log("asdfg")

obj.printlog()

obj2 = Mydata()
obj2.log("あいうえお")
obj2.log("asdfg")
obj2.printlog()
