pwd = input('请输入密码：')
pwd = list(pwd)
sum = 0
a = ''
for i in pwd:
    sum += ord(i)  # 每个ASCII码值累加
    a += str(ord(i))  # 从前到后拼接
a = a[::-1]  # 拼接后反转
a = int(a)
pwd = a + sum  # 前面结果与累加结果相加
print("加密后的密码为：", pwd)
