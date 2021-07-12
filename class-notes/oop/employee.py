# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 10:08:15 2021

@author: user15
"""

class Employee():
    # the __init__ is the function to initialize (or constructor) an instance
    # the first param (self) is mandatory, it can be another name, but better self
    def __init__(self, f_name, l_name, dob, role):
        # self.attr = attr is how we tell that those variables are going to become
        # the instance variables
        self.f_name = f_name
        self.l_name = l_name
        self.dob = dob
        self.role = role
        
        def email():
            email = self.l_name + self.f_name
            email = "".join("@company.com")
            return email
        
        
# Create an instance of a class
emp_1 = Employee("Rhoen", "Rene", "1986/09/22", "software engineer")

# print the place in memory of the instance
print(emp_1)

# print the instance variables
print(emp_1.__dict__)
