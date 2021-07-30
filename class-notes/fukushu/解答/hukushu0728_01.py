import matplotlib.pyplot as plt

y = []
count = 0

while True:
    num = input("数値を入力：")
    
    if num == "end":
        break
    else:
        try:
            num = int(num)
            y.append(num)
            count += 1
        except ValueError:
            print("数値を入力してください。")
        except Exception:
            print("エラーが発生しました。")

x = [str(i) for i in range(1, count + 1)]
plt.plot(x, y)
plt.show()