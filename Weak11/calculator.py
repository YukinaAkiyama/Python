import tkinter as tk

# 窗口
window = tk.Tk()
window.title('计算器')
window.geometry('500x150')

# 数字1输入框
entry_number1 = tk.Entry(window)
entry_number1.pack(fill='x', side='left')

# 标签 符号+
tk.Label(window, text='+').pack(fill='x', side='left')

# 数字2输入框
entry_number2 = tk.Entry(window)
entry_number2.pack(fill='x', side='left')

# 标签 符号=
tk.Label(window, text='=').pack(fill='x', side='left')

# 答案输入框
entry_number3 = tk.Entry(window)
entry_number3.pack(fill='x', side='left')


# 计算函数
def calculate():
    # 输入框获取计算数据
    number1 = float(entry_number2.get())
    number2 = float(entry_number1.get())
    answer = number1 + number2

    entry_number3.delete(0, 66)
    entry_number3.insert("insert", str(answer))


# 退出的函数
def calculate_quit():
    window.destroy()


# 计算 退出按钮
bt_login = tk.Button(window, text='计算', command=calculate)
bt_login.place(x=200, y=120)

bt_logquit = tk.Button(window, text='退出', command=calculate_quit)
bt_logquit.place(x=290, y=120)
# 主循环
window.mainloop()
