import tkinter as tk

# 创建窗口
window = tk.Tk()
window.title('My window')  # 窗口的标题
window.geometry('400x100')  # 窗口的大小
# 定义一个label
l1 = tk.Label(window,
              text='为什么我的眼里常含泪水',  # 标签的文字
              bg='green',  # 标签背景颜色
              font=('Arial', 12),  # 字体和字体大小
              width=20, height=2,  # 标签长宽(以字符长度计算)
              )
l1.pack(side='top')  # 固定窗口位置

# 定义一个label
l2 = tk.Label(window,
              text='因为我对这土地爱的深沉',  # 标签的文字
              bg='blue',  # 标签背景颜色
              font=('Arial', 12),  # 字体和字体大小
              width=20, height=2,  # 标签长宽(以字符长度计算)
              )
l2.pack(side='bottom')  # 固定窗口位置

window.mainloop()
