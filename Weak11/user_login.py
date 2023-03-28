import tkinter as tk
import tkinter.messagebox

# 窗口
window = tk.Tk()
window.title('登录')
window.geometry('450x250')

# 标签 用户名密码
tk.Label(window, text='用户名:').place(x=100, y=50)
tk.Label(window, text='密码:').place(x=100, y=90)
# 用户名输入框
var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=50)
# 密码输入框
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=90)


# 登录函数
def usr_log_in():
    # 输入框获取用户名密码
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    global count
    count = 0

    # 用户名密码不能为空
    if usr_name == '' or usr_pwd == '':
        tk.messagebox.showerror(message='用户名或密码为空')
    # 判断用户名和密码是否匹配
    elif usr_name == 'abcdefg':
        if usr_pwd == '123456':
            tk.messagebox.showinfo(title='welcome',
                                   message='欢迎您：' + usr_name)
        else:
            tk.messagebox.showerror(message='密码错误')
    else:
        if count < 3:
            print(count)
            tk.messagebox.showerror(message='用户名错误')
            count = count + 1
            print(count)
        else:
            tk.messagebox.showerror(message='错误三次，禁止输入')



# 退出的函数
def usr_sign_quit():
    window.destroy()


# 登录 注册按钮
bt_login = tk.Button(window, text='登录', command=usr_log_in)
bt_login.place(x=160, y=130)

bt_logquit = tk.Button(window, text='退出', command=usr_sign_quit)
bt_logquit.place(x=260, y=130)
# 主循环
window.mainloop()
