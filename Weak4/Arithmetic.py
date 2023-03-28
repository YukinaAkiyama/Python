import random

print("十以内四则运算\n共十道题\n总分一百分\n")
correct = 0
incorrect = 0
for i in range(10):
    a = random.randint(0, 10)
    t = random.choice("+-*/")
    b = random.randint(0, 10)
    print(a, t, b, "=")
    answer = eval(input())
    if t == "+":
        if answer == a + b:
            print("正确")
            correct += 1
        elif answer != a + b:
            print("错误")
            incorrect += 1
    elif t == "-":
        if answer == a - b:
            print("正确")
            correct += 1
        elif answer != a - b:
            print("错误")
            incorrect += 1
    elif t == "*":
        if answer == a * b:
            print("正确")
            correct += 1
        elif answer != a * b:
            print("错误")
            incorrect += 1
    elif t == "/":
        if answer == a / b:
            print("正确")
            correct += 1
        elif answer != a / b:
            print("错误")
            incorrect += 1

print("做了%s道题\n正确%s道\n错误%s道\n最终得分：%s" % ((correct + incorrect), correct, incorrect, (correct*10)))
