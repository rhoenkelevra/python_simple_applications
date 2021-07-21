# -*- coding: utf-8 -*-

from good_property2 import Goods2
from goods_property import Goods
from override import Greet2
from super1 import Player
from car_class1 import Car

car1 = Car()
car2 = Car("red")
car3 = Car("black")
car1.mileage = 10_000
print(car1)  # returns the __str__() instead of memory location
print(car2)  # returns the __str__() instead of memory location

# インスタンスの変数を更新する
car1.color = "green"
car1.mileage = 100

print(car1, car2)
print(car1.color, car1.mileage)

# インスタンスメソッドを実行する
car1.drive(15)
car2.drive(100)
car1.drive(40)

# ===========================================
# クラスメンバー

print(Car.maker, Car.count)
car1.maker = "toyota"
print(car1.maker)
print(car2.maker)
# the instance can change it's value for the class attributes
# but changes is only for itself, not all instances
# to change all:
# Car.maker = "toyota"

# ===========================================
# ClassMethods
print(car1.mynumber, car2.mynumber, car3.mynumber)

# ===========================================
# Pg286
# 作った後から変数とメソッドを追加する


class Simple:
    pass


Simple.x = 100
Simple.x *= 2

print(Simple.x)


def hello(msg="ハロー"):
    print(msg)


Simple.greeting = hello
Simple.greeting("おはよう！")
print(Simple.greeting)

obj = Simple()
obj.a = 123
print(obj.a)
print(obj)

obj1 = Simple()
obj2 = Simple()


def drum(beat="トコトコ"):
    print(beat)


def sax(phrase="プープー"):
    print(phrase)


obj1.play = drum
obj2.play = sax

print(obj1.play, obj2.play)

# 追加したメンバーを削除する
obj1.a = None
obj1.play = None
del Simple.x

# ==================================================================
# Chapter 12 - 2


class A:
    def hello(self):
        print("Hello")


class B(A):
    def bye(self):
        print("bye")


obj = B()
obj.hello()
obj.bye()
# ==================================================================
# Pg291

obj = Greet2()
obj.hello("井上")
obj.hello()

# ==========================================================================
# Pg 293

player1 = Player("青木", 16, 10, "MF")

print(player1.name)
print(player1.age)
print(player1.number)
print(player1.position)

# ==================================================================
# Chapter 12 -3

shoes = Goods("dream", 6800, "shoes")
print(shoes.name)
shoes.name = "Dream 8"
print(shoes.name)
print(shoes.price)
hat = Goods("hat", 500, "hat")
del shoes
print(shoes)

del hat.name  # Can't delete attribute
shoes.price = 5000  # Can't set attribute
print(shoes.price)
