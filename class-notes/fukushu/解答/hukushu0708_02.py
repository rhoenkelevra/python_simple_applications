# アルゴリズムテキスト　練習6
# 正の整数を2つ受付け、加算した数値が「3の倍数」かつ「2の倍数」であったときのみ出力する
# 条件に合わなかった場合は"規格外"と出力する

x = int(input("整数1を入力："))
y = int(input("整数2を入力："))

kaitou = x + y

if kaitou % 3 == 0 and kaitou % 2 == 0:
    print(kaitou)
else:
    print("規格外")
