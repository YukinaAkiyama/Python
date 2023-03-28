import random

verificationCode = ""
for i in range(4):
    verificationCode += chr(
        random.choice([random.randint(65, 90), random.randint(97, 122), random.randint(ord("0"), ord("9"))]))
print(verificationCode)
userEnter = input("请输入验证码：")
if userEnter == verificationCode:
    print("正确")
else:
    print("错误")
