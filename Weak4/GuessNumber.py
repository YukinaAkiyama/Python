import random

guessNumber = random.randint(1, 100)
print("猜数游戏开始\n你一共有五次机会\n范围是1~100")
for i in range(5):
    playerNumber = int(input("请输入你的数字:\n"))
    if playerNumber < guessNumber:
        print("小了，你应该猜大一点:-(")
        print("你还有%d次机会" % (4 - i))
    elif playerNumber > guessNumber:
        print("大了，你应该猜小一点:-(")
        print("你还有%d次机会" % (4 - i))
    else:
        print("猜对了，恭喜你:-)")
        break
else:
    print("失败超过五次，请重新开始游戏")
