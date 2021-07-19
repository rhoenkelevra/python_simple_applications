# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 10:25:21 2021

@author: user24
"""

# Pg250
import exchange
yen = 25000
rate = 114.22
charge = 1.0
dollar = exchange.yen2dollar(yen, rate, charge)

print(f"{dollar :,.2f} ドル")

# モジュールを再読み込みする　(Reload Module)
# In case the module has change, we reload it to get new newest one

import importlib
importlib.reload(exchange)



# =============================================================================

# Pg253

import os
curr_dir = os.getcwd()

# =============================================================================

# Pg254
# DocString 

def cheer(who = 'kun'):
    
    '''
    This is a description of this method
    '''
    
    print(who + "はスゴイ！最高だ！")
    
    
help(cheer) # shows the method and it's docstring

