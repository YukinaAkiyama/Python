from tkinter import *

root = Tk()

menubar = Menu(root)


def callback():
    pass


menubar.add_command(label="复制", command=callback)
menubar.add_command(label="粘贴", command=callback)

frame = Frame(root, width=512, height=512)
frame.pack()


def popup(event):
    menubar.post(event.x_root, event.y_root)


frame.bind("<Button-3>", popup)

mainloop()
