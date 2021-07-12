# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 09:33:36 2021

@author: user15
"""
cnt = 0
sum2 = 0
while cnt < 100:
    cnt +=2
    sum2 += cnt 
    
print("-" * 10,"\n",sum2)


cnt = 0
sum2 = 0
while cnt < 100:
    if cnt % 2 == 0:

        sum2 += cnt 
     
    cnt += 1
    print(cnt)
    
print("-" * 10,"\n",sum2)
        