import tkinter as tk

# 窗口
window = tk.Tk()
window.title('Find Popups')
window.geometry('300x310')


def find_mes():
    window_find = tk.Toplevel(window)
    window_find.geometry('200x150')
    window_find.title("Find")
    # 输入框
    tk.Entry(window_find).place(x=30, y=20)
    # 查找按钮
    bt_confirm_sign_up = tk.Button(window_find, text='查找')
    bt_confirm_sign_up.place(x=85, y=90)


# 查找按钮
bt_login = tk.Button(window, text='查找', command=find_mes)
bt_login.place(x=138, y=10)
# 文本框
text = tk.Text(window, width=300, height=300)
text.insert("insert", "这是一首简单的小情歌")
text.place(x=0, y=45)

window.mainloop()
