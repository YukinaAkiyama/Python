import tkinter as tk

# 创建窗口


window = tk.Tk()
window.title('My window')  # 窗口的标题
window.geometry('400x300')  # 窗口的大小
# 定义一个label
l1 = tk.Label(window,
              text='确定要退出此窗口吗',  # 标签的文字
              # 标签背景颜色
              font=('Arial', 12),  # 字体和字体大小
              width=20, height=2,  # 标签长宽(以字符长度计算)
              )
l1.pack(side='top')  # 固定窗口位置


# 按钮操作
def hit_me2():
    exit()


# 按钮1
b1 = tk.Button(window,
               background='green',  # 颜色
               text='退出',  # 显示在按钮上的文字
               width=15, height=2,
               command=hit_me2,
               )  # 点击按钮式执行的命令
b1.pack(fill='x', side='right')  # 按钮位置
# 按钮2
b2 = tk.Button(window,
               background='red',  # 颜色
               text='我再想想吧',  # 显示在按钮上的文字
               width=15, height=2,
               )  # 点击按钮式执行的命令
b2.pack(fill='x', side='right')  # 按钮位置

window.mainloop()
