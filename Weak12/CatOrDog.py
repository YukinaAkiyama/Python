from tkinter import *

window = Tk()
window.geometry("310x150")


def selection():
    if radio.get() is 1:
        selection = "答错了，答案是修狗，因为旺旺仙贝（汪汪先背）"
        label.config(text=selection)
    elif radio.get() is 2:
        selection = "恭喜你，答对了！"
        label.config(text=selection)


radio = IntVar()

lbl = Label(text="猫猫还是修狗:")
lbl.pack()

R1 = Radiobutton(window, text="猫猫", variable=radio, value=1)
R1.place(x=50, y=55)

R2 = Radiobutton(window, text="修狗", variable=radio, value=2)
R2.place(x=50, y=90)

buttonOk = Button(window, text='提交', command=selection)
buttonOk.place(x=130, y=125, width=50, height=20)

label = Label(window)
label.pack()

window.mainloop()
