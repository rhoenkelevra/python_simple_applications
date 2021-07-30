# ① 「calculation.py」を読み込む
import calc

# ②  利用者から数値を２つ受取る
num1 = input("ひとつ目の数値：")
num2 = input("ふたつ目の数値：")

# ③  数値変換を行う
num1 = int(num1)
num2 = int(num2)

# ④  4つの関数を発動し戻り値を受取る
ans1 = calc.add(num1, num2)
ans2 = calc.sub(num1, num2)
ans3 = calc.mul(num1, num2)
ans4 = calc.div(num1, num2)

# ⑤ 「◯算の結果は：△」の形で関数の数、出力する
print(f"加算の結果：{ans1}")
print(f"減算の結果：{ans2}")
print(f"乗算の結果：{ans3}")
print(f"除算の結果：{ans4}")








