# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 10:37:30 2021
question from codewars
@author: user24
"""

# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new string with all vowels removed.

# best answer 
# def disemvowel(s):
    # return s.translate(None, "aeiouAEIOU")

def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    str_split = [char for char in string_]
    no_vowels_list = [str for str in str_split if not str in vowels]
    string_final = "".join(no_vowels_list)
        
            
    return string_final


x = disemvowel("This website is for losers LOL!")
print(x)