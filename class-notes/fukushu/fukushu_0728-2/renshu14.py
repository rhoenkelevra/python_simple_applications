<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 14:06:22 2021

@author: user24
"""

'''
 renshu14.py の仕様 
  実行ファイルとして処理を記述していく 
 1. CoinCase クラスのインスタンスを作成する。 
 2. 種類と枚数を入力し、add_coins メソッドで硬貨を追加することを 10 回繰り返す。 
 3. 各硬貨が何枚あるかを表示する。 
 4. 総額を表示する。 
'''


from CoinCase import CoinCase
coin_case = CoinCase(
    {1: 0,
     5: 0,
     10: 0,
     50: 0,
     100: 0,
     500: 0
     })

while True:
    print("硬貨の種類は：　１、５、１０,１００、５００")
    koka = input("硬貨の種類は？ \n--> ")
    if koka == "q":
        break
    qnt = input("硬貨の枚数は？ \n--> ")

    try:
        coin_case.add_coins(int(koka), int(qnt))
    except:
        print("数値で入れてください!!")
        continue

coin_case.get_count()
print("=" * 20)
coin_case.get_total()
=======
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 14:06:22 2021

@author: user24
"""

'''
 renshu14.py の仕様 
  実行ファイルとして処理を記述していく 
 1. CoinCase クラスのインスタンスを作成する。 
 2. 種類と枚数を入力し、add_coins メソッドで硬貨を追加することを 10 回繰り返す。 
 3. 各硬貨が何枚あるかを表示する。 
 4. 総額を表示する。 
'''


from CoinCase import CoinCase
coin_case = CoinCase(
    {1: 0,
     5: 0,
     10: 0,
     50: 0,
     100: 0,
     500: 0
     })

while True:
    print("硬貨の種類は：　１、５、１０,１００、５００")

    try:
        koka = input("硬貨の種類は？ \n--> ")
        if koka == "q":
            break
        koka = int(koka)

        qnt = input("硬貨の枚数は？ \n--> ")
        if qnt == "q":
            break
        qnt = int(qnt)

    except ValueError:
        print("数値で入れてください!!")
        continue
    except Exception as error:
        print(error)

    # coin_case type's is class, so use the __dict__ to transform into dict
    # then the first value is it's name {'coin_case': {1: 0, .. }}
    if int(koka) in coin_case.__dict__['coin_case']:
        coin_case.add_coins(koka, qnt)
    else:
        print("Error")


coin_case.get_count()
print("=" * 20)
coin_case.get_total()
>>>>>>> 74819e2c355b4194e7fa01491dc63ef8b5a1a986
