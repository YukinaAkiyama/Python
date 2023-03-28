import random

score: list = []
for i in range(1, 11):
    print("第", i, "位学生成绩：")
    a = random.randint(0, 100)
    score.append(a)

print("\n这十位学生成绩：")
print(score)

max = score[0]
Location = 0
for i in score:
    if i > max:
        max = i
        Location += 1
print("最高分：", max, "位置：", Location)
