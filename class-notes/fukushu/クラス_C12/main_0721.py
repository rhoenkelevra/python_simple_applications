# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 09:32:45 2021

@author: user24
"""
'''
pythonのファイルを２つ作成し、プログラムを完成させなさい。


【input_save.py	InputSaveクラスを持つモジュール】

	① InputSaveクラスを定義

	② 引数を１つ受け取る初期化メソッドを定義

	   初期化メソッドは受け取った引数をインスタンス変数「input_save」に格納する



【renshu12.py	「input_save.py」モジュールを使用し処理を行う実行プログラム】

	① 「input_save.py」を読み込む

	②  利用者からデータを１つ受け取る

	③  受け取ったデータを使用しInputSaveのインスタンスを作成

	    インスタンス内にデータが保存されること

	④ 「入力したデータは：◯◯です。」の形でインスタンス変数のデータを出力

'''


from input_save import InputSave


ans = input("データを入力してください  \n -->")

ans_inst = InputSave(ans)

print(ans_inst.input_save)




# ans_list = []
# while True:
#     ans = input("データを入力してください  \n-->　")
    
#     if ans == "q":
#         break
    
#     ans_inst = InputSave(ans)
    
#     ans_list.append(ans_inst)
    

# for ans in ans_list:
#     print(ans)






