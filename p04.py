import math

for i in range(900, 1000):
    for j in range(i, 1000):
        n = i*j
        num = str(n)
        pal = True
        for k in range(0, int(math.floor(len(num) / 2))):
            if num[k] != num[len(num) - 1 - k]:
                pal = False
                break
        int1 = str(i)
        int2 = str(j)
        if pal:
            print int1 + ", " + int2 + ", " + num
