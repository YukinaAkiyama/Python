import random


def judge(num1, num2, s) -> int:
    if s == '+':
        return num1 + num2
    elif s == '-':
        return num1 - num2
    elif s == '*':
        return num1 * num2
    elif s == '/':
        return num1 / num2
    else:
        print("输入错误")
        return 0


count = 0
operator_table = "+-*/"
while count < 20:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(operator_table)
    text_n = str(num1) + operator + str(num2) + "=" + "\n"
    with open("questions.text", "a") as w:
        w.write(text_n)
    text_t = str(num1) + operator + str(num2) + "=" + '{:.2f}'.format(judge(num1, num2, operator)) + "\n"
    with open("answer.text", "a") as w:
        w.write(text_t)
    count += 1
