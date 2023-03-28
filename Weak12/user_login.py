import tkinter
import tkinter.messagebox
import random

class LoginPage(object):

    def __init__(self):
        # 声明两个变量
        self.win = tkinter.Tk()  # 窗口
        self.username = tkinter.StringVar()
        self.password = tkinter.StringVar()
        self.txt = tkinter.StringVar()
        self.n = 2
        self.createForm()
        var = self.text_code

    def login(self):
        if self.username.get() == '123' and self.password.get() == '123':
            print('登录成功')
            tkinter.messagebox.showinfo(title='登录信息', message='登录成功')
            self.win.quit()
        else:
            tkinter.messagebox.showerror(title='登录信息', message='登录失败，你还有' + str(self.n) + '次机会')
            if self.n == 0:
                tkinter.messagebox.showinfo(title='登录信息', message='用户名或密码错误三次，你没有权限进入该系统')
                self.win.quit()
        self.n -= 1

    # 随机数实现6位验证码。
    def createCode(self):
        res = ''
        for i in range(2):
            num = random.randint(0, 9)
            res += str(num)
            num = random.randint(65, 90)
            res += str(chr(num))
            num = random.randint(97, 122)
            res += str(chr(num))
        string = str(res)
        str_list = list(string)  # 将循环到的6位字符串转化为列表
        random.shuffle(str_list)  # 用列表的shuffle函数随机打乱
        shuffle_str = ''.join(str_list)  # 连接列表中6位字符
        self.txt.set(shuffle_str)
        return self.txt

    # 确认按钮功能
    def confirm(self):
        t1 = self.get()
        t2 = text_code.get()
        if t1.upper() == t2.upper() or t1.lower() == t2.lower():  # 忽略大小写
            messagebox.showinfo('window', '验证成功')  # 弹出提示框
        else:
            messagebox.showerror('window', '验证失败')

    def createForm(self):
        self.win.title('登录界面')
        # 创建标签
        labelname = tkinter.Label(self.win, text='用户名：', justify=tkinter.RIGHT, width=80)
        # 将标签放置在窗口上
        labelname.place(x=10, y=20, width=80, height=20)
        # 创建文本框
        entryname = tkinter.Entry(self.win, width=80, textvariable=self.username)
        entryname.place(x=100, y=20, width=80, height=20)
        # 创建密码标签
        labelpwd = tkinter.Label(self.win, text='密   码：', justify=tkinter.RIGHT, width=80)
        labelpwd.place(x=10, y=45, width=80, height=20)
        # 创建密码的文本框
        entrypwd = tkinter.Entry(self.win, width=80, textvariable=self.password)
        entrypwd.place(x=100, y=45, width=80, height=20)

        code = tkinter.Label(self.win, text='验证码：', fg='black', bg='turquoise')
        code.place(x=25, y=70, width=50, height=20)
        self.text = tkinter.Entry(self.win)
        self.text.place(x=100, y=70, width=80, height=20)

        self.txt.set('获取验证码')
        codestr = tkinter.Button(self.win, textvariable=self.txt, command=self.createCode, fg='black')
        codestr.place(x=40, y=95, width=115, height=20)
        text_code = self.txt

        buttonName = tkinter.Button(self.win, text='检测', command=self.confirm, fg='blue', bg='lightblue')
        buttonName.place(x=75, y=120, width=50, height=30)

        # 创建button按钮
        buttonOk = tkinter.Button(self.win, text='登录', command=self.login)
        buttonOk.place(x=40, y=155, width=50, height=20)

        # 创建退出的按钮
        buttonQuit = tkinter.Button(self.win, text='退出', command=self.win.quit)
        buttonQuit.place(x=100, y=155, width=50, height=20)

        self.win.mainloop()


if __name__ == '__main__':
    lg = LoginPage()
