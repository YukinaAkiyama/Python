import random


class Verification:
    def __init__(self):
        self.code = []

    @staticmethod
    def upperCase():
        choice = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
                 "abcdefghijklmnopqrstuvwxyz" \
                 "1234567890"
        return random.choice(choice)

    def creatCode(self):
        for i in range(6):
            self.code.append(self.upperCase())
        random.shuffle(self.code)
        return ''.join(self.code)


if __name__ == '__main__':
    verification = Verification()
    print('验证码：', verification.creatCode())
