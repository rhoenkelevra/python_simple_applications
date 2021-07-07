# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 12:21:28 2021

@author: user15
"""

from random import choice

counter = 0
def randomize():
    jokenpo_value = ['gu', 'choki', 'pa']
    machine = choice(jokenpo_value)
    return machine

# get input from user
def init_game(counter):
    
    if counter == 0: 
        user = input("Ｊｏｋｅｎｐｏ！　\n ==>")
        randomize()
        check(user, randomize(), counter)
        return user
    elif counter >= 1:
        user = input("Aiko desho \n ==>")
        randomize()
        check(user, randomize(), counter)
        return user
        
# check if user vs machine
def check(user_input, machine, counter):
    if user_input == machine:
        counter += 1
        init_game(counter)
        
    elif ((user_input == 'gu' and machine == 'choki') or (user_input == 'choki' and machine == 'pa') or (user_input == 'pa' and machine == 'gu')):
        print("user win")
    elif ((user_input == 'gu' and machine == 'pa') or (user_input == 'pa' and machine == 'choki') or (user_input == 'choki' and machine == 'gu')):
        print("machine win")


init_game(counter)
