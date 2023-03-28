import tkinter as tk

root = tk.Tk()
root.geometry("400x400")

label_1 = tk.Label(root, text="测试你性格有几面\n当你看不惯别人的行为时,你会直接指出吗?", bg="white")
label_1.pack()

v = tk.IntVar()

tk.Radiobutton(root, text="一定会", value=1, variable=v,
               indicatoron=False, width=25, pady=3).pack(padx="0.1i", pady="0.1i")
tk.Radiobutton(root, text="很可能会", value=2, variable=v,
               indicatoron=False, width=25, pady=3).pack(padx="0.1i", pady="0.1i")
tk.Radiobutton(root, text="偶尔会", value=3, variable=v,
               indicatoron=False, width=25, pady=3).pack(padx="0.1i", pady="0.1i")
tk.Radiobutton(root, text="绝不会", value=4, variable=v,
               indicatoron=False, width=25, pady=3).pack(padx="0.1i", pady="0.1i")


def show():
    if v.get() is 1:
        selection = "老实？"
        label.config(text=selection)
    elif v.get() is 2:
        selection = "好嘛！"
        label.config(text=selection)
    elif v.get() is 3:
        selection = "要得！"
        label.config(text=selection)
    elif v.get() is 4:
        selection = "你说是，就是吧！"
        label.config(text=selection)
    else:
        selection = "就这？"
        label.config(text=selection)


button_1 = tk.Button(root, text="提交", bg="white", command=show)
button_1.pack()

label = tk.Label(root)
label.pack()


root.mainloop()
