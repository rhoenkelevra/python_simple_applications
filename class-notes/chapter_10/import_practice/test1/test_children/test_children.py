# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 11:15:44 2021

@author: user24
"""

def average(*args):
    if args:
        ave = sum(args) / len(args)
        return ave
    else:
        return None
    