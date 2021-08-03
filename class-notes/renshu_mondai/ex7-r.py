import math


r = float(input("半径を入力してください。："))

# 円の面積 circle_S
circle_S = math.pi*r*r

# 円周 L
L = 2*math.pi*r

# 球の体積 V
V = 4/3*math.pi*r**3

# 球の表面積 S
S = 4*math.pi*r**2

print("円の面積："+str(round(circle_S, 2)))
print("円周："+str(round(L, 2)))
print("球の体積："+str(round(V, 2)))
print("球の表面積："+str(round(S, 2)))
