dlist = []

while True:
    inp = input("追加：1\t表示：2\t終了：3 > ")
    
    if inp == "3":
        break
    
    if inp == "1":
        data = input("データを入力してください。 > ")
        dlist.append(data)
    elif inp == "2":
        ref = int(input("表示する要素を指定してください。 > "))
        
        if -len(dlist) <= ref < len(dlist):
            print(dlist[ref])
