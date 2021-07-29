# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 13:27:12 2021

@author: user24
"""

import sys
if len(sys.argv) < 2:
    print("読み込むファイル名指定してください")
    sys.exit()

file = sys.argv[1]
with open(file) as fileobj:
    text= fileobj.read()
    print(text)













