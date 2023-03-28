import tkinter as tk1
import tkinter.messagebox
import tkinter.ttk
import pickle

# import ui.Main_UI as mu

# 窗口
root = tk1.Tk()
root.title('欢迎')
root.geometry('690x500')
print('hello')


# 登录函数
def usr_log_in():
    # 输入框获取用户名密码
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    # 从本地字典获取用户信息，如果没有则新建本地数据库
    try:
        with open('usr_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usr_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
    # 判断用户名和密码是否匹配
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk1.messagebox.showinfo(title='welcome',
                                    message='欢迎您：' + usr_name)
            root.destroy()

        else:
            tk1.messagebox.showerror(message='密码错误')
    # 用户名密码不能为空
    elif usr_name == '' or usr_pwd == '':
        tk1.messagebox.showerror(message='用户名或密码为空')
    # 不在数据库中弹出是否注册的框
    else:
        is_signup = tk1.messagebox.askyesno('欢迎', '您还没有注册，是否现在注册')
        if is_signup:
            usr_sign_up()  # 打开注册界面


# 注册函数
def usr_sign_up():
    # 确认注册时的相应函数
    def signtowcg():
        # 获取输入框内的内容
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_pwd_confirm.get()

        # 本地加载已有用户信息,如果没有则已有用户信息为空
        try:
            with open('usr_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info = {}

            # 检查用户名存在、密码为空、密码前后不一致
        if nn in exist_usr_info:
            tk1.messagebox.showerror('错误', '用户名已存在')
        elif np == '' or nn == '':
            tk1.messagebox.showerror('错误', '用户名或密码为空')
        elif np != npf:
            tk1.messagebox.showerror('错误', '密码前后不一致')
        # 注册信息没有问题则将用户名密码写入数据库
        else:
            exist_usr_info[nn] = np
            with open('usr_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk1.messagebox.showinfo('欢迎', '注册成功')
            # 注册成功关闭注册框
            window_sign_up.destroy()

    # 新建注册界面
    window_sign_up = tk1.Toplevel(root)
    window_sign_up.geometry('350x200')
    window_sign_up.title('注册')
    # 用户名变量及标签、输入框
    new_name = tk1.StringVar()
    tk1.ttk.Label(window_sign_up, text='用户名：').place(x=10, y=10)
    tk1.ttk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=10)
    # 密码变量及标签、输入框
    new_pwd = tk1.StringVar()
    tk1.ttk.Label(window_sign_up, text='请输入密码：').place(x=10, y=50)
    tk1.ttk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=150, y=50)
    # 重复密码变量及标签、输入框
    new_pwd_confirm = tk1.StringVar()
    tk1.ttk.Label(window_sign_up, text='请再次输入密码：').place(x=10, y=90)
    tk1.ttk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*').place(x=150, y=90)
    # 确认注册按钮及位置
    bt_confirm_sign_up = tk1.ttk.Button(window_sign_up, text='确认注册', command=signtowcg)
    bt_confirm_sign_up.place(x=150, y=130)


# 界面
def display():

    # 封面
    pic_label = tk1.Label

    # 标签 用户名密码
    tk1.ttk.Label(root, text='用户名:').place(x=240, y=320)
    tk1.ttk.Label(root, text='密码:').place(x=240, y=360)
    # 用户名输入框
    global var_usr_name
    var_usr_name = tk1.StringVar()
    entry_usr_name = tk1.ttk.Entry(root, textvariable=var_usr_name)
    entry_usr_name.place(x=300, y=320)
    # 密码输入框
    global var_usr_pwd
    var_usr_pwd = tk1.StringVar()
    entry_usr_pwd = tk1.ttk.Entry(root, textvariable=var_usr_pwd, show='*')
    entry_usr_pwd.place(x=300, y=360)
    # 登录 注册按钮
    bt_login = tk1.ttk.Button(root, text='登录', command=usr_log_in, width=6)
    bt_login.place(x=250, y=400)
    bt_logup = tk1.ttk.Button(root, text='注册', command=usr_sign_up, width=6)
    bt_logup.place(x=320, y=400)
    bt_logquit = tk1.ttk.Button(root, text='退出', command=exit, width=6)
    bt_logquit.place(x=390, y=400)

    root.mainloop()


if __name__ == '__main__':

    display()
    # root.wait_window()
    # mu.display_top()
