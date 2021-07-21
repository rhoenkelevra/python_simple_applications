dlist = []
count = 0

while count < 10:
    inp = input("データを入力してください。 > ")
    
    if not inp:
        continue
    
    dlist.append(inp)
    count += 1
    
while True:
    inp = input("入力順：1　昇順：2　降順：3　終了：4 > ")
    
    if inp == "4":
        break
    
    if inp == "1":
        for i, data in enumerate(dlist, 1):
            print(f"{i}:{data}")
    elif inp == "2":
        for i, data in enumerate(sorted(dlist, key = str.lower), 1):
            print(f"{i}:{data}")
    elif inp == "3":
        for i, data in enumerate(sorted(dlist, reverse = True, key = str.lower), 1):
            print(f"{i}:{data}")
