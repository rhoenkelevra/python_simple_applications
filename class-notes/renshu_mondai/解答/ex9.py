#住所録追加
def addAddress(name,address,tel,mail):
    item = [name,address,tel,mail]
    addressList.append(item)
    print("登録しました。")
    print()

#住所録表示
def showAddress(addressNum):
    obj = addressList[addressNum-1]
    print("名前：" + obj[0])
    print("住所：" + obj[1])
    print("電話番号：" + obj[2])
    print("メールアドレス：" + obj[3])
    print()

#住所録検索
def searchAddress(search):
    addressListCnt = len(addressList)
    count = 0
    if addressListCnt == 0:
        print("住所録が未登録です。")
        return
    for i in range(addressListCnt):
        checkFlg = False
        for j in range(len(addressList[i])):
            if search in addressList[i][j]:
                checkFlg = True
        if checkFlg == True:
            print("名前："+ addressList[i][0])
            print("住所："+ addressList[i][1])
            print("電話番号："+ addressList[i][2])
            print("メールアドレス："+ addressList[i][3])
            print()
            count += 1
    if count > 0:
        print(str(count) + "件のデータが見つかりました。")
        print()
    else:
        print("入力された「 " +str(search) +" 」が含まれるデータは見つかりませんでした。")
        print()
                
            
        
print("住所管理アプリケーションへようこそ。")
addressList = []
while True:   
    print("**********メニュー**********")
    menu = input("1)住所録追加 2)住所録表示 3)住所録検索 9)終了：")
       
    if menu == '1':
        print("住所録に登録するデータを入力してください。")
        name = input("名前：")
        address = input("住所：")
        tel = input("電話番号：")
        mail = input("メールアドレス：")
        addAddress(name,address,tel,mail)
        continue
       
    elif menu == '2':
        addressListCnt = str(len(addressList))
        if addressListCnt == '0':
            print("住所録が未登録です。")
            print()
            continue
        else:
            addressNum = int(input("表示するアドレスの番号を入力してください。（1-" + addressListCnt + ")："))
            print()
            showAddress(addressNum)
            continue

    elif menu == '3':
        search = input("検索するデータを入力してください：")
        print()
        searchAddress(search)
        continue

    else:
        print("ありがとうございました。")
        
    break
   


