"""
本程序旨在用泰勒级数完成对lnx的近似估计，注:本程序存在局限性，因为当迭代次数较多时，每次迭代产生的数值会很大以至于溢出，故只能求解0~2之间的ln值
"""
import math as m

print('本程序计算lnx的值')
x = float(input('请输入x:'))
n = 1
s = x - 1
a = []
# sum1 = 0
while m.fabs(s) >= m.pow(10, -5):
    a.append(s)
    n = n + 1
    s = pow(-1, n - 1) * 1.0 / n * pow(x - 1, n)
#     sum1 = sum1 + 1
# print("迭代次数是:", sum1)
sum = 0
for i in range(0, n - 1):
    sum = sum + a[i]

print('ln(' + str(x) + ')的近似值为', sum)
