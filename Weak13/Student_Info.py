from tkinter import *

root = Tk()
root.title('学生信息管理')
student_info = Menu(root)
menubar = Menu(root)


def callback():
    pass


openVar = IntVar()
saveVar = IntVar()
quitVar = IntVar()

filemenu = Menu(student_info, tearoff=False)
filemenu.add_checkbutton(label='打开', command=callback, variable=openVar)
filemenu.add_checkbutton(label='保存', command=callback, variable=saveVar)
filemenu.add_separator()
filemenu.add_checkbutton(label='退出', command=root.quit, variable=quitVar)
student_info.add_cascade(label='文件', menu=filemenu)

editVar = IntVar()

editmenu = Menu(student_info, tearoff=False)
editmenu.add_radiobutton(label="剪贴", command=callback, variable=editVar, value=1)
editmenu.add_radiobutton(label="复制", command=callback, variable=editVar, value=2)
editmenu.add_radiobutton(label="粘贴", command=callback, variable=editVar, value=3)
student_info.add_cascade(label="编辑", menu=editmenu)

root.config(menu=student_info)

menubar.add_command(label="复制", command=callback)
menubar.add_command(label="粘贴", command=callback)

frame = Frame(root, width=512, height=512)
frame.pack()


def popup(event):
    menubar.post(event.x_root, event.y_root)


frame.bind("<Button-3>", popup)

mainloop()
