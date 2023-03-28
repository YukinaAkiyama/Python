import random

answer1 = [2, 4, 9, 11, 12, 30]
answer2 = [1]

redBalls = []
for i in range(0, 6):
    red = random.randint(1, 33)
    redBalls.append(red)
redBalls.sort()
print("红球选取结果：", redBalls)

blueBall = [random.randint(1, 16)]
print("篮球选取结果：", blueBall)

count = 0
for number in redBalls:
    if number in answer1:
        count += 1
print("红球中奖数：", count)
if count == 6 and blueBall == answer2:
    print("一等奖：500万元")
elif count == 6:
    print("二等奖：10万元")
elif count == 5 and blueBall == answer2:
    print("三等奖：3000元")
elif count == 5 or count == 4 and blueBall == answer2:
    print("四等奖：200元")
elif count == 4 or count == 3 and blueBall == answer2:
    print("五等奖：10元")
elif blueBall == answer2:
    print("六等奖：5元")
else:
    print("没中奖，欢迎下次光临！")

print("程序结束")
