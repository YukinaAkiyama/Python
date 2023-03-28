import random

item = "a"
num = ["apple", "banana", "orange"]

new = chr(ord(item)+3)
low = random.choice(num)
up = random.choice(num).upper()
password = low + up + new
s1 = "Python"
uppers1 = s1.upper()
print(uppers1)
lowers1 = s1.lower()
print(lowers1)
capitalizes1 = s1.capitalize()
print(capitalizes1)

name = "赵钱孙李周吴郑王"
for i in range(len(name)):
    print(name[i], end=" ")
for index, i in enumerate(name):
    print(index+1, i, end=" ")