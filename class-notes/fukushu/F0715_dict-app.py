# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 11:21:25 2021

@author: user15
"""
# =============================================================================
# 
# 登録: 1
# 検索: 2
# 一覧: 3
# 終了: 4
# 
# toroku
# 単語を入力しください　英字で入力すること
# 和語を入力
# back to menu
# 
# 検索
# 単語を入力しください　英字で入力すること
# 
# 一覧
# show all entries
# 
# 
# =============================================================================

words = {}

while True:
    inp = input("登録: 1 検索: 2 一覧: 3 終了: 4 削除：　５ \n-->")
    
    if inp == "4":
        break
        
    try:
        if inp == "1":
            register_input_1 = input("単語を入力しください　(英字で入力すること) \n-->")
            if register_input_1 == "":
                continue 
            
            register_input_2 = input("和語を入力\n-->")
            if register_input_1 == "":
                continue 
            
            words[register_input_1] = register_input_2
            print(words)
            continue
    
        if inp == "2":
            search_input = input("単語を入力しください　(英字で入力すること) \n-->")
            print(words[search_input])
            
        if inp == "5":
            search_input = input("単語を入力しください　(英字で入力すること) \n-->")
            if words[search_input]:
                words.pop(search_input)
            
    except KeyError:
        print("この単語がありあません。")
    except Exception as error:
        print(error)
        
    if inp == "3":
        print(words)
        for i, (key, value) in enumerate(words.items(), 1):
            print(f"{i}-> {key}: {value}")
       