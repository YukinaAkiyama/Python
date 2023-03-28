import math

for i in range(1, 100001):
    a = int(math.sqrt(i + 100))
    b = int(math.sqrt(i + 100 + 268))
    if a * a == (i + 100) and b * b == (i + 100 + 268):
        print(i)
