import string


class Calculator:

    @staticmethod
    def plus(num1, num2):
        return num1 + num2

    @staticmethod
    def minus(num1, num2):
        return num1 - num2

    @staticmethod
    def multiply(num1, num2):
        return num1 * num2

    @staticmethod
    def divide(num1, num2):
        return num1 / num2


if __name__ == '__main__':

    calculator = Calculator()
    while True:
        x = eval(input("输入数字一："))
        y = eval(input("输入数字二："))

        print("请选择运算符：‘+’、‘-’、‘*’、‘/’")
        print("或按Q退出")
        symbol: string = input()
        print("你选择的是：%s" % symbol, "号")
        if symbol == '+':
            print(x, ' + ', y, ' = ', calculator.plus(x, y))
        elif symbol == '-':
            print(x, ' - ', y, ' = ', calculator.minus(x, y))
        elif symbol == '*':
            print(x, ' * ', y, ' = ', calculator.multiply(x, y))
        elif symbol == '/':
            print(x, ' / ', y, ' = ', calculator.divide(x, y))
        elif symbol == 'Q' or 'q':
            exit()
        else:
            print("错误！")
