score: list = []
for i in range(1, 6):
    print("输入第", i, "位学生成绩：")
    a = eval(input())
    score.append(a)

print("这五位学生成绩：")
for i in score:
    print(i, "\n")

print(score)
