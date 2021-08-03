total = 0
count = 0
while True:
    num = input("入力してください。：")
    if num == "End":
        break
    total += int(num)
    count += 1
print(str(count)+"回入力しました。")
print("合計は"+str(total)+"です。")