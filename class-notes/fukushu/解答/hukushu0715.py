dictionary = dict()

while True:
    inp = input("登録：1　検索：2　一覧：3　終了：4 > ")
    
    if inp == "4":
        break
    
    if inp == "1":
        key = input("単語を入力（英字で入力すること） > ")
        if key == "":
            continue

        data = input("和訳を入力 > ")
        if data == "":
            continue

        dictionary[key] = data
        
    elif inp == "2":
        key = input("単語を入力（英字で入力すること） > ")
        if key in dictionary:
            print(f"{key}：{dictionary[key]}")
    
    elif inp == "3":
        for en, ja in dictionary.items():
            print(f"{en}：{ja}")

