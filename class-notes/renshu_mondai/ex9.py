# -*- coding: utf-8 -*-
class AddressBook:
    contact_list = []
    
    def __init__ (self, name, jusho, denwa, email):
        self.name = name
        self.jusho = jusho
        self.denwa = denwa
        self.email = email
      
#  住所録追加 
    @classmethod
    def add_contact(cls, name, jusho, denwa, email):
        # インスタンスを作る
        c = AddressBook(name, jusho, denwa, email)
        
        # リストにインスタンスを入れる
        AddressBook.contact_list.append(c)
        print("登録しました。")
        print()
        return AddressBook.contact_list


    # 住所録表示
    @classmethod
    def get_all_contact(cls):
        for c in AddressBook.contact_list:
            print(f"名前:{c.name}")
            print(f"住所:{c.jusho}")
            print(f"電話番号:{c.denwa}")
            print(f"メールアドレス:{c.email}")
            print("*" * 20)
        

    # 住所録検索

    def search(keyword):
        # 何件を見つけるのカウンター
        count = 0
        
        # インスタンスにあるリストにループ
        for c in AddressBook.contact_list:
            # インスタンスループ
            for k, v in c.__dict__.items(): 
                if keyword in v:
                    count += 1
                    print(f"名前:{c.name}")
                    print(f"住所:{c.jusho}")
                    print(f"電話番号:{c.denwa}")
                    print(f"メールアドレス:{c.email}")
                    print("*" * 20)
                    print(f"{count}件のデータが見つかりました。 ")
          
while True:
    print("**********メニュー**********")
    choice = input("1)住所録追加 2)住所録表示 3)住所録検索 9)終了:  ")
    
    # プログラム終了
    if choice == "9":
        print("ありがとうございました。")
        break
    
    # 追加する
    if choice == "1":
        name = input("名前:  ")
        jusho = input("住所:  ")
        denwa = input("電話番号:  ")
        email = input("メールアドレス:  ")
        AddressBook.add_contact(name, jusho, denwa, email)
        
    # 全部う参照する
    if choice == "2":
        AddressBook.get_all_contact()   
        
    # KEYWORDで検索
    if choice == "3":
        search_item = input("検索するデータを入力してください:  ")
        AddressBook.search(search_item)  
        
'''
Data structure of the contact list 
contact_list = [{"name": "", "address": "", "denwa": "", "meru": ""},
                {{"name": ""}, {"address": ""}, {"denwa": ""}, {"meru": ""} }
                ]
'''

'''
演習9
■ 仕様 
住所録を管理するコンソールアプリケーションを作成してください。 
実行すると、ウェルカムメッセージとメニューを表示します。
○ 画面イメージ 
------------------------------------
住所管理アプリケーションへようこそ。
**********メニュー**********
1)住所録追加 2)住所録表示 3)住所録検索 9)終了:
------------------------------------
● 住所録追加 
この機能は、名前、住所、電話番号、メールアドレスを住所録としてリストに登録します。なお、名前、住所、
電話番号は必須項目とします。
○ 画面イメージ 
------------------------------------
住所録に登録するデータを入力してください。
名前:前園
住所:岐阜県各務原市 
電話番号:058-321-4567 
メールアドレス:maezono@XXX.YYY 
登録しました。 
------------------------------------
その後、メニューを表示します。
● 住所録表示 
この機能は、指定した番号の住所録データを画面に表示します。
○ 画面イメージ
------------------------------------
表示するアドレスの番号を入力してください。(1-5):5
名前:前園
住所:岐阜県各務原市 
電話番号:058-321-4567 
メールアドレス:maezono@XXX.YYY 
------------------------------------
アドレスの番号は 1~件数とします。 
その後、メニューを表示します。

● 住所録検索 
この機能は、指定した文字列を含む住所録データを画面に表示します。
○ 画面イメージ 
------------------------------------
検索するデータを入力してください:愛知県
名前:山田 
住所:愛知県名古屋市 
電話番号:090-1111-xxxx 
メールアドレス:abc@xxx.yyy

名前:佐藤 
住所:愛知県犬山市 
電話番号:080-0000-xxxx 
メールアドレス:xyz@xxx.yyy
2 件のデータが見つかりました。 
------------------------------------
その後、メニューを表示します。
● 終了
○ 画面イメージ
------------------------------------
ありがとうございました。 
------------------------------------
その後、アプリケーションを終了します。
'''