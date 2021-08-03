i = 3
while i >= -3:
    if i < 0:
        n = i * -1
    else:
        n = i
    j = 0
    while j < n:
        print("○",end="")
        j += 1
    print()
    i -= 1
