# -*- coding: utf-8 -*-


from random import randint 

def dice():
    num = randint(1, 6)
    return num

for i in range (5):
    result = dice(5)
    print(result)
from random import randint

def dice():
    num = randint(1, 6)
    return num

for i in range(5):
    dice1 = dice()
    dice2 = dice()
    sum = dice1 + dice2
    print(f"{dice1} and {dice2} de kaikei {sum}")
    
# =============================================================================
    
# Pg 235
def mile2meter(mile):
    meter = mile * 1609.344
    return meter

distance = mile2meter(20)
print(distance)
print(mile2meter(30))

# =============================================================================
# Pg236
def triangle(base, height):
    area = base * height / 2
    return area

b = 15
h = 13
v = triangle(b, h)

print(f"底辺{b}、高さ{h}の参画型の面積は {v :.1f}です。")

# =============================================================================
# Pg237
from random import randint
def dice():
    num = randint(1, 6)
    return num

def dicegame():
    dice1 = dice()
    dice2 = dice()
    
    sum = dice1 + dice2
    
    if sum%2 == 0:
        print(f"{dice1}と{dice2}で合計{sum}、　偶数")
    else:
        print(f"{dice1}と{dice2}で合計は{sum}、奇数")
    
for i in range(5):
    dicegame()
print("ゲーム終了")
    
# Pg 238
def calc(num):
    unit_price = 180
    if not num.isdigit():
        return None
    price = int(num) * unit_price
    return price

while True:
    num = input("個数を入れてください。　（ｑ　で終了）")
    if num == "":
        continue
    elif num == "q":
        break
    
    result = calc(num)
    print(result)
    
# =========================================================================

# 07/16　復習
# 関数とは　。。。　処理の集まりです
# 繰り返しと使用する。
# 処理をまとめ
 
# 戻り値：　関数の処理結果

# 引数：　関数を呼び出す時使用する値
# 
 # foo bar baz
 # hoge fuga piyo
#　
# 復讐問題０７１６
def addition(n1, n2):
    return n1 + n2

value = addition(10,20)
print(value)

def calc(operator, n1, n2):
     if operator == 1:
         return n1 + n2
     if operator == 2:
         return n1 - n2
     if operator == 3:
         return n1 * n2
     if operator == 4:
         return n1 / n2
     else:
         print("Enter digits")
x = calc("a", 2, 3) 
print("result:", x)

#  Using dictionay instead of if
def calc2(ope, n1, n2):
    return {
        1: n1 + n2,
        2: n1 - n2,
        3: n1 * n2,
        4: n1 / n2
        }.get(ope)
y = calc2(1, 4, 5)
print(y)


# because is not returning a value, as the funtion is called, it will print
# and x will be none, can't s
def sum(n1, n2):
    print(n1 + n2)

x = sum(1, 2)
print("x",x)

def compare(n1, n2):
    if n1 == n2:
        return True
    else: 
        return False
    

x = compare(1, 1)
print(x)

# =============================================================================

# Pg239 
def calc(num):
    unit_price = 180
    try:
        num = float(num)
        return num * unit_price
    except:
        return None
  
    
while True:
    num = input("個数を入れてください。　（ｑ　で終了）")
    if num == "":
        continue
    elif num == "q":
        break
    
    result = calc(num)
    print(result)
# =============================================================================
# Pg240
#　有効範囲　

v = 2 # グローバル変数

def calc():
    # v = 2  # ローカル変数
    # v = v * 10 (UnboundLocalError: local variable 'v' referenced before assignment) it's trying to make a calculation before it know's it's value
    # v = 1 CAN reassign variable
    x = v * 10 
    ans = 3 * x
    print(ans)

calc()
print(v)
