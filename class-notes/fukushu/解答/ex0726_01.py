
total = 0

while True:
    s = input("数値を入力>>>")
    n = int(s)
    if n == 0:
        break
    total += n
    
print("合計は" + str(total) + "です。")