# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 15:23:41 2021

@author: user24
"""
# Pg290
# Inheritance
from datetime import datetime
class Datalog:
    def __init__(self):
        self.loglist = []
        
    def log(self, data):
        now = datetime.now()
        item = (now, data)
        self.loglist.append(item)