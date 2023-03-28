import tkinter as tk
from tkinter import messagebox

# 窗口

window = tk.Tk()
window.title('Find Popups')
window.geometry('300x300')


def info_pop():
    messagebox.showinfo('温馨提示', '这是消息提示框')


def waring_pop():
    messagebox.showwarning('操作警示', '这是消息警告框')


def error_pop():
    messagebox.showerror('操作警示', '这是错误消息框')


def askquestion_pop():
    messagebox.askquestion('确认操作', '确认执行此次操作吗？')  # 返回值yes/no


# 按钮
info_button = tk.Button(window, text='消息提示框', command=info_pop)
info_button.place(x=120, y=10)

waring_button = tk.Button(window, text='消息警告框', command=waring_pop)
waring_button.place(x=120, y=40)

error_button = tk.Button(window, text='错误消息框', command=error_pop)
error_button.place(x=120, y=70)

askquestion_button = tk.Button(window, text='关闭消息框', command=askquestion_pop)
askquestion_button.place(x=120, y=100)

window.mainloop()
