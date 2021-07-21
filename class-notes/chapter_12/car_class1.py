# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 14:35:19 2021

@author: user24
"""


class Car:
    # Class variables
    maker = "PEACE"
    count = 0

    # 初期化メソッド
    def __init__(self, color='white'):
        Car.countup()
        self.mynumber = Car.count
        self.color = color or 'white`'
        self.mileage = 0

    # defines a method to print the instances as STRING
    # without it when print(instance) -> memory location
    # good to have! returns a description of the attributes
    def __str__(self):
        return f"color: {self.color}, mileage: {self.mileage}"

    def drive(self, km):
        self.mileage += km
        msg = f"{km}kmドライブしました。総距離は{self.mileage}kmです。"
        print(msg)

    @classmethod
    def countup(cls):
        cls.count += 1
        print(f"出荷台数：　{cls.count}")
