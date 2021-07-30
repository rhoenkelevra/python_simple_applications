# 解法1
# dset = set()
# count = 0

# while True:
# 	data = input("データを入力してください。('q'を入力すると終了) >")
# 	
# 	if data == "q":
# 		break
# 	
# 	dset.add(data)
# 	count += 1

# print(f"入力回数は{count}回でした。")
# print(f"重複を除去したデータは{len(dset)}個でした。")


# 解法2
# dlist = []

# while True:
# 	data = input("データを入力してください。('q'を入力すると終了) >")
# 	
# 	if data == "q":
# 		break
# 	
# 	dlist.append(data)

# print(f"入力回数は{len(dlist)}回でした。")
# print(f"重複を除去したデータは{len(set(dlist))}個でした。")

