
tate = int(input("タテ："))
yoko = int(input("ヨコ："))

print("模様を入力してください（空白を入力して終了）")

pList = None #パターンリストの初期化
max = 0 #模様の最大文字数

while  True:
    pattern = input()
    if len(pattern) > 0: #模様が入力された場合の繰り返し処理
        if pList == None:
            pList = [0]
        else:
            nowpList = [0] #模様一時保管用パターンリスト
            nowpList = nowpList*(len(pList)+1)
            for i in range(len(pList)):
                nowpList[i] = pList[i]
            pList = nowpList
        pList[len(pList)-1] = pattern #入力された模様をPListの末尾に代入
        if max < len(pattern):
            max = len(pattern)
    else:
        break


#模様の入力が済んだ後（空白を入力後）の処理
tex = [[0 for i in range(max)] for i in range(len(pList))] #出力用リスト(tex)　模様の種類分の要素にネストした、模様の文字数分の要素の2次元リストを内包表記で作成

for i in range(len(tex)):
    for j in range(max):
        if j < len(pList[i]):
            tex[i][j] = pList[i][j:j+1] #PListから一文字ずつ出力用リストに移し替え
        else:
            tex[i][j] = "　"


for i in range(tate):
    for j in range(yoko):
        print(tex[i % len(tex)][j % len(tex[0])],end="")
    print()