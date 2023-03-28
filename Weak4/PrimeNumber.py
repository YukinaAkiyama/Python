from math import sqrt

for x in range(2, 101):  # 因为range函数终止值不包括在内，所以写到101
    flag = 1  # 利用flag以防止出错
    k = int(sqrt(x))
    for i in range(2, k + 1):
        if x % i == 0:
            flag = 0
            break
    if flag:
        print(x, end=' ')