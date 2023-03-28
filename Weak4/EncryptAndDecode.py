print("请选择进行加密还是解密"
      "\n1.加密"
      "\n2.解密"
      "\n3.退出")
choice = eval(input("请输入选项："))
str_1: str = ""
if choice == 1:
    str_2: str = input("请输入需要加密的密码，6~18位，且为纯字母：")
    if 6 <= len(str_2) <= 18:
        print("你输入的是：", str_2)
    else:
        print("密码不符合规范")
    for i in range(len(str_2)):
        a = ord(str_2[i])
        str_1 += chr(a + 5)
    print("加密后：", str_1)

if choice == 2:
    str_2: str = input("请输入需要解密的密码，6~18位，且为纯字母：")
    if 6 <= len(str_2) <= 18:
        print("你输入的是：", str_2)
    else:
        print("密码不符合规范")
    for i in range(len(str_2)):
        a = ord(str_2[i])
        str_1 += chr(a - 5)
    print("解密后：", str_1)

if choice == 3:
    exit()
