# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 13:23:23 2021

@author: user24
"""

'''
Trying to make a factory function like in JS
Create instances and append them to a list
'''

from car_class1 import Car


cars = []
def factory(color, mileage = 0):
    car = Car(color, mileage)
    cars.append(car)

factory("blue")
factory("black", 500)

c = 0
for car in cars:
    c += 1
    print(c, car.__dict__)
    
    
def delete(id):
    cars.remove(cars[id])
    

delete(0)
for car in cars:
    c += 1
    print(c, car.__dict__)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    