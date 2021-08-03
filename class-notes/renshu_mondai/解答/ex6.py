tate = int(input("タテの値を入力してください。"))
yoko = int(input("ヨコの値を入力してください。"))
for i in range(tate):
    for j in range(yoko):
        if (i % 2 + j) % 2 == 0:
            print("#",end="")
        else:
            print(".",end="")
    print("")