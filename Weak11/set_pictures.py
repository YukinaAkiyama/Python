import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('1024x512')
root.title('Test')
root.resizable(False, False)

global photo
# 设置条形框,插入图片
image1 = Image.open("96251354_p0_master1200.png")
photo1 = ImageTk.PhotoImage(image1)
Lab = tk.Label(root, compound='left', image=photo1)
Lab.pack(fill='x', side='left')  # 设置主界面

# 设置条形框,插入图片
image2 = Image.open("85100907_p0_master1200.jpg")
photo2 = ImageTk.PhotoImage(image2)
Lab = tk.Label(root, compound='right', image=photo2)
Lab.pack(fill='x', side='left')  # 设置主界面

root.mainloop()
