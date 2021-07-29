# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 13:56:20 2021

@author: user24
"""
# Goal:
# Print 5 lines of 10 random float numbers with 2 decimal precision
from random import uniform

# generate one line of random floats
def create_list(min, max, dig):
    n_row = []
    for n in range(max):
        n = round(uniform(min, max), dig)
        n_row.append(n)
   
    return n_row

# ==========================================================================
# run func 5 times to create lines
cnt = 0  
txt = []      
while cnt < 6:
    
    txt += create_list(1, 5, 2)
    cnt += 1

# ==========================================================================
# convert list to string
#TODO not working! 
# remove [] from the string 
newtxt = txt.pop[0]
txt = str(txt)    

txt = "".join(txt)   

print(type(txt))
print(txt)

# ==========================================================================
# Write in file

# file = "./data/nums.txt"
# with open(file, "w") as fileobj:
    
#     fileobj.write(txt)
    
    



# for l in range(6):
#    for n in range(5):
#        n = round(uniform(1,5), 2) 
#        n_row.append(n)
   
#    num_lis.append(n_row)
#    n_row = []
   

