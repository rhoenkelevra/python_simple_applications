# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 12:33:43 2021

@author: user15
"""
import string
from random import choice

pass_size = int(input("暗証番号の長さを記入して下さい \n -->"))
# ask user if wants uppercase letters and symbols

use_symbols = input("暗証番号には記号も使いますか　（Y か　N): \n -->")

def containsLetterAndNumber(input):
    return any(x.isalpha() for x in input) and any(x.isnumeric() for x in input)

def write_to_file(password, question):
    if question.upper() == "Y":
        pass_name = input("この暗証番号はどこで使いますか。: \n -->")
        # if file is not on same dir as .py, put the 
        file1 = open(r"pass.txt", 'a')
        file1.write(f"{pass_name} <===>  {password} \n")
        file1.close()
        
        print("暗証番号はpass.textに保存済み")
    else:
        print(f"暗証番号は{password}、忘れないで下さい。")


def generate_pass(size=pass_size, symbols=use_symbols):
    if symbols.upper() == 'N' :
        chars = string.ascii_letters + string.digits
    elif symbols.upper() == 'Y':
        chars = string.ascii_letters + string.digits + string.punctuation
        
    temp_chars = "".join(choice(chars) for _ in range(size))
    
    if containsLetterAndNumber(temp_chars):
        print("おすすめの暗証番号は：", temp_chars)
        question_save = input("pass.txtファイルに保存しますか （Y か　N): \n -->")
        write_to_file(temp_chars, question_save)
        
    else:
        print('not good pass, generate again!')
        generate_pass()
         
        
        
generate_pass()



