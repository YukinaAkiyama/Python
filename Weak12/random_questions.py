# from tkinter import *
import random
import tkinter as tk

correct = 0  # 记录正确的数量
total = 0  # 记录总数量
errorList = []
t_total = 0
allProblem = []


def getProblem():
    a = random.randint(1, 18)
    if a < 10:
        b = random.randint(10 - a, 9)
        c = a + b
        result = "%d  +  %d" % (a, b)  # 题目生成
        allProblem.append(result)
        # print(result)
        return result, c
    if a >= 10:
        b = random.randint(a - 9, 9)
        c = a - b
        result = "%d  -  %d" % (a, b)  # 题目生成
        allProblem.append(result)
        # print(result)
        return result, c  # 返回的题目 && 答案


def check():
    global t_total
    t_total -= 1
    if int(result.get()) == int(t[1]):
        global correct
        correct += 1
        h = "恭喜你！回答正确"
        hint.set(h)
    else:
        h = "糟糕！回答错误！"
        errorList.append(t[0])  # 将错误的编号假加入 记录错误题目列表
        hint.set(h)
        result.set('')  # 设置为空串


def showAllProblemInPage():  # 在界面展示所有的题目
    var1 = len(allProblem) // 2
    var2 = 2

    def confirmRC():
        global var1, var2
        var1 = hang.get()
        var2 = lie.get()
        var1 = int(var1)
        var2 = int(var2)  # print(var1) print(var2)
        disPlayWindow = tk.Tk()
        disPlayWindow.title('所有题目如下：')
        disPlayWindow.geometry('800x800+100+100')

        display = ''  # 展示的字符串
        cnt = 0
        for i in allProblem:
            cnt += 1
            if cnt % var2 != 0:
                display = display + i + '\t' + '\t'
            else:
                display = display + i + '\n'
        lb = tk.Label(disPlayWindow, bg='pink', width=150, height=50)
        lb.config(text=display)
        lb.grid(row=1, column=1)

    # 注意下行数和列数
    windowAllProblem = tk.Tk()
    windowAllProblem.title('所有题目展示界面')
    windowAllProblem.geometry('300x300+100+100')

    # 行数列数标签放置
    l1 = tk.Label(windowAllProblem, text='行数：')
    l1.grid(row=0)
    l2 = tk.Label(windowAllProblem, text='列数：')
    l2.grid(row=1)

    hang = tk.Entry(windowAllProblem, show=None)
    hang.grid(row=0, column=1)
    lie = tk.Entry(windowAllProblem, show=None)
    lie.grid(row=1, column=1)
    # 行列放置完成
    confirmBtn = tk.Button(windowAllProblem, text='确认行和列', command=confirmRC)
    confirmBtn.grid(row=2, column=1)
    # 行数列数已经获取 :
    # var1 行数 var2 列数
    print(var1)
    print(var2)
    windowAllProblem.mainloop()


def showWrongProblemInPage():  # 将所有错误题目在界面展示
    var1 = len(errorList) // 2
    var2 = 2

    def confirmRC():
        global var1, var2
        var1 = hang.get()
        var2 = lie.get()
        var1 = int(var1)
        var2 = int(var2)  # print(var1) print(var2)
        disPlayWindow = tk.Tk()
        disPlayWindow.title('所有题目如下：')
        disPlayWindow.geometry('800x800+100+100')

        display = ''  # 展示的字符串
        cnt = 0
        for i in errorList:
            cnt += 1
            if cnt % var2 != 0:
                display = display + i + '\t' + '\t'
            else:
                display = display + i + '\n'
        lb = tk.Label(disPlayWindow, bg='pink', width=150, height=50)
        lb.config(text=display)
        lb.grid(row=1, column=1)
        # print(display)

    # 注意下行数和列数
    windowAllProblem = tk.Tk()
    windowAllProblem.title('所有题目展示界面')
    windowAllProblem.geometry('300x300+100+100')

    # 行数列数标签放置
    l1 = tk.Label(windowAllProblem, text='行数：')
    l1.grid(row=0)
    l2 = tk.Label(windowAllProblem, text='列数：')
    l2.grid(row=1)

    hang = tk.Entry(windowAllProblem, show=None)
    hang.grid(row=0, column=1)
    lie = tk.Entry(windowAllProblem, show=None)
    lie.grid(row=1, column=1)
    # 行列放置完成
    confirmBtn = tk.Button(windowAllProblem, text='确认行和列', command=confirmRC)
    confirmBtn.grid(row=2, column=1)
    # 行数列数已经获取 :
    # var1 行数 var2 列数
    windowAllProblem.mainloop()
    print(var1)
    print(var2)


def calCorrectRate():
    global total, correct
    # 定义一下 正确率
    correct_rate = correct / total
    correct_rate = correct_rate * 100.0
    correct_rate = str(correct_rate) + ' %'
    return correct_rate


def next():
    global t, t_total

    l.config(text='一共需要做 ' + str(total) + ' 道题\n' + '还剩' + str(t_total) + ' 道题\n')
    t = getProblem()
    problem.set(t[0])
    result.set('')
    hint.set('')  # 判断的结果置为空


def getNumber():
    global total, t_total
    total = int(number.get())
    t_total = total
    # print(t_total) #输出总共的题目数量
    var1.set(str(total))
    # print(var1)
    l.config(text='一共需要做 ' + str(t_total) + ' 道题\n')
    # print(total)


master = tk.Tk()
master.geometry('500x400+100+100')
master.title("加减进退位运算")
var1 = tk.StringVar()  # 定义一个变量
l = tk.Label(master, bg='yellow', width=30)  # text-variable=var1,
l.grid(row=18)  # 放置在第18行
tk.Label(master, text='请输入数量：').grid(row=0)  # 放置在第一行，这个框里面的是
tk.Label(master, text="题目").grid(row=1)
tk.Label(master, text="答案").grid(row=2)
tk.Label(master, text="信息").grid(row=5)

problem = tk.StringVar()
result = tk.StringVar()
hint = tk.StringVar()  # 记录答案是否正确

number = tk.Entry(master, show=None)
number.grid(row=0, column=1)
e1 = tk.Entry(master, textvariable=problem)  # 题目显示
e2 = tk.Entry(master, textvariable=result)  # 答案框显示
e3 = tk.Entry(master, textvariable=hint)  # 结果显示

t = getProblem()
problem.set(t[0])  # 作为题目problem
result.get()

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=5, column=1)

btn0 = tk.Button(master, text='确认数量', command=getNumber)
btn = tk.Button(master, text='确定', command=check)  # 执行 check函数
btn2 = tk.Button(master, text='下一题', command=next)  # 执行 下一个题
# 窗口放置
btn0.grid(row=0, column=4)
btn.grid(row=2, column=4)
btn2.grid(row=2, column=5)

master.mainloop()
