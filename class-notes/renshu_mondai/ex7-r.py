import math


#円の面積
def circ_area(r):
    r = int(r)
    return math.pi * r * r

#円周
def circumference(r):
    r = int(r)
    return 2 * math.pi * r

#球の体積
def sphere(r):
    r = int(r)
    return 4/3 * math.pi * r ** 3

#球の表面積
def surface(r):
    r = int(r)
    return 4 * math.pi * r ** 2


r = float(input("半径を入力してください。："))

print("円の面積："+str(round(circ_area(r), 2)))
print("円周："+str(round(circumference(r), 2)))
print("球の体積："+str(round(sphere(r), 2)))
print("球の表面積："+str(round(surface(r), 2)))