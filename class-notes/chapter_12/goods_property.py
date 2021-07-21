# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 13:43:19 2021

@author: user24
"""

# Pg. 297, 298
# プロパティのゲッター、セッターを指定する


class Goods:

    count = 0

    def __init__(self, name, price):
        Goods.countup()
        # initialize with a protect dict called __data
        # 非公開のインスタンス変数
        self.__data = {"name": name, "price": price}
        self.mynumber = Goods.count

    @classmethod
    def countup(cls):
        cls.count += 1
    # Decorator for get

    @property
    def name(self):
        ''' Get the private name att'''
        # get the "name" and return it
        return self.__data["name"]

    # Decorator for set -> the name is the same as method and the att to avoid confusion
    # Can change the name, but when called it, have to use the proper name
    @name.setter
    def name(self, value):
        ''' Sets the private name att to a new value '''
        # setter: set "name" to new value
        self.__data["name"] = value

    @property
    def price(self):
        '''Get the price and return formated in jp format '''

        # getter: get the protected "price" value
        price = self.__data["price"]
        # format it to fstring and return it
        price_str = f"{price:,}円。"
        return price_str

    # Without the setter, the price is READ ONLY

    # @price.setter
    # def price(self, value):
    #     self.__data["price"] = value

    # # Avoid Deleter
    # @property.deleter
    # def name(self):
    #     raise AttributeError("Don't delete this")
