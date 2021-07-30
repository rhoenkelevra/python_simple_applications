# 入力回数を数えるやり方
# total = 0
# cnt = 0
# while True:
#     s = input("数値を入力>>>")
#     n = int(s)
#     if n == 0:
#         break
#     total += n
#     cnt += 1
    
    
# print("合計は" + str(total) + "です。")
# avg = total / cnt
# print("平均は" + str(avg) + "です。")

# リストに入力値をすべて入れる

#total = 0
nums = []

while True:
    s = input("数値を入力>>>")
    n = int(s)
    if n == 0:
        break
    #total += n
    nums.append(n)

total = sum(nums)
avg = total / len(nums)
print("合計は" + str(total) + "です。")
print("平均は" + str(avg) + "です。")







