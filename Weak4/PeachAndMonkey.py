day = eval(input("请输入摘几天："))
num = 2
sum = num
for i in range(1, day):
    num *= 2
    num += 1
    sum += num
print("一共摘了%s个"%sum)