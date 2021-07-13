# Pg 168
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 09:05:12 2021

@author: user15
"""

# Pg 168
numbers = [15, 23, 4, 41, 8, 16]
numbers.sort()
print(numbers)


numbers = [15, 23, 4, 42, 8, 16]
numbers.sort(reverse = True)
print(numbers)

letters = ['a', 'b', 'g', 'd', 'e', 'c','f']
letters.sort()
print(letters)

words = ["peach", "ver3", "Python", "Pokemon", "ver2"]
words.sort()
print(words)


# Make new list
numbers = [15, 23, 4, 41, 8, 16]
number_ascend = sorted(numbers)
print(number_ascend)
print(numbers)

numbers_descend = sorted(numbers, reverse = True)
print(numbers_descend)

## Reverse the list
numbers = [15, 23, 4, 42, 8, 16]
numbers.reverse()
print(numbers)

## Shuffle
import random 
numbers = list(range(10))
random.shuffle(numbers)
print(numbers)

### Use  ??

words = ["chest", "wind", "holiday", "knight", "silence", "hot"]
words.sort(key = len)
print(words)

words = ["peach", "ver3", "Python", "Pokemon", "ver2"]
new_words = sorted(words, key = str.lower)
print(new_words)
