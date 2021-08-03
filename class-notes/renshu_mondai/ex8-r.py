#BMI指数計算
def bmiCalc(height,weight):
    return weight / (height**2)

#標準体重計算
def sWeightCalc(height):
    return  (height**2) * 22

#肥満度計算
def bodyMassIndexCalc(height,weight):
    sWeight = sWeightCalc(height)
    return (weight - sWeight) / sWeight * 100


while True:   
    print("健康管理アプリケーションへようこそ。")
    name = input("名前を入力してください：")
    height = float(input("身長（m）を入力してください："))
    weight = float(input("体重（kg）を入力してください："))

    while True:
        print("**********メニュー**********")
        menu = input("1)BMI指数計算 2)標準体重計算 3)肥満度計算 9)終了：")
        bmi = 0
        mes= ""
        sWeight = 0

        if menu == "1":
            bmi = bmiCalc(height,weight)
            if bmi > 25.0:
                mes = "ふとっています。"
            elif bmi >= 18.5:
                mes = "ふつうです。"
            else:
                mes = "やせています。"

            print("BMI指数は{0:.1f}です。{1}さんは{2}".format(bmi,name, mes))
            print()
            continue

        elif menu == "2":
            sWeight = sWeightCalc(height)
            print("{0}さんの標準体重は{1:.1f}です。".format(name, sWeight))
            print()
            continue

        elif menu == "3":
            bodyMassIndex = bodyMassIndexCalc(height,weight)
            if bodyMassIndex > 20.0:
                mes = "肥満です。"
            elif bodyMassIndex >= 10.0:
                mes = "肥満気味です。"
            else:
                mes = "肥満ではありません。"
            print("肥満度は{0:.0f}%です。{1}さんは{2}".format(bodyMassIndex,name, mes))
            print()
            continue

        else:
            print("ありがとうございました。")
            
        break
    break
   


