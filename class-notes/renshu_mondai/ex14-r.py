#計算用関数
def subset_sum(d,numbers, target, partial=[]): #d,numbers（1からnまでの値のリスト）,target（合計x）,partial（取り出した値の組み合わせリスト）
    s = sum(partial) #取り出した組み合わせの合計を求める
    result = "" #結果出漁用変数初期化
    # 組み合わせの合計（s）がtarget（xの値）と等しいかどうかを確認
    if s == target: 
        if len(partial) == d: #組み合わせの内、dの数の組み合わせのみ出力
           for i in range(len(partial)):
               result += str(partial[i])
               if i == (len(partial)-1):
                   result += " = "+str(target)
               else:
                   result += " + "
        print(result)
            
    if s >= target:
        return  # sがx以上の場合は呼出しもと（for文内のsubset_sum関数）にリターンする

    for i in range(len(numbers)): #1からnまでの値を順番に取り出す
        n = numbers[i] #numbersのiの値を取り出す
        remaining = numbers[i+1:] #残りの値をスライスし、リストに格納する
        subset_sum(d,remaining, target, partial + [n]) #subset_sum関数を再帰呼び出しし、第2引数にはnumbersの取り出した残りのリスト（remaining）を渡し、第4引数には組み合わせの合計を求めるリストpartial）に1つずつ取り出したnumbersの値のリスト(n)を連結



#実行プログラム
n = int(input("n="))
d = int(input("d="))
x = int(input("x="))
numbers = []

#1からnの数をリストnumbersに格納
for i in range(n):
    numbers.append(i+1)

subset_sum(d,numbers,x)

