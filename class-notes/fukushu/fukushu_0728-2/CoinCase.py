# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 14:05:50 2021

@author: user24
"""

'''

 CoinCase クラスの基本仕様  500 円、100 円、50 円、10 円、5 円、1 円が、それぞれ何枚あるかインスタンス変数で管理。 
 add_coins メソッドで硬貨を追加する。 引数は硬貨の種類と枚数の 2 つのデータ。 
 get_count メソッドで、指定した硬貨が、何枚あるかを取得する。  引数は硬貨の種類、戻り値は枚数の 2 つのデータ。 
 get_amount メソッドで硬貨の総額を取得する。 
 戻り値は硬貨の総額の 1 つのデータ。 ※硬貨の種類は 500 円なら整数の 500、100 円なら 100 とし、該当しない数が指定された場合には無視する。 

'''


class CoinCase:
    total = 0

    def __init__(self, coin_case):
        self.coin_case = coin_case

    def add_coins(self, coin_type, amount):
        self.coin_case[coin_type] = amount
        return self.coin_case

    def get_count(self):
        for k, v in self.coin_case.items():
            print(f'{k}円は{v}枚')

    def get_total(self):
        total = 0
        for k, v in self.coin_case.items():
            self.sum = (k * v)
            total += self.sum
        print(f'合計は：{total}')
