# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 11:42:12 2021

@author: user15
"""

# =============================================================================
# モージュールを読み込む
# =============================================================================

import math
from random import randint as dice, random


# print(secret)

# print(math.ceil(15.2))  # 切り上げ

# print(math.floor(15.2))  # 切り捨て

# print(math.pi)

# print(round(math.pi, 2))

# print(math.degrees(math.pi / 4))

# kyori = 20
# kakudo = math.radians(32)
# takasa = kyori * math.tan(kakudo)
# takasa = math.floor(takasa * 100) / 100
# print(str(takasa) + "m")

# =============================================================================
#  Random
# =============================================================================

# print(randint(1, 6))

print(random())

print(dice(1, 10))

char = 'qo1'
print(char.isalnum())