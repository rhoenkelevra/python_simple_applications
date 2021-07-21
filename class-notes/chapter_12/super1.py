# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 11:23:32 2021

@author: user24
"""

# Pg293, 294
# スーパークラスの初期化メソッドに引数を渡す
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Player(Person):
    # def __init__(self, number, position): # Ｐｅｒｓｏｎクラスの初期化メソッドをオーバーライドする
    def __init__(self, name, age, number, position):
    # スーパークラス初期化メソッドを使うため、　super().__init__(引数１、引数２)
    #               スーパークラスに引数の値を渡す
        super().__init__(name, age) #スーパークラスの初期化メソッドを呼び出す 
        self.number = number
        self.position = position
        
