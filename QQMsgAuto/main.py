# coding = utf-8
import random
import time
from io import BytesIO  # python3,新增字节流

import win32api
import win32clipboard as clipboard
import win32con
import win32gui
from PIL import Image
from pynput.keyboard import Controller as kController

print("循环开始！")
while True:
    keyboard = kController()


    # 定义指定图片文件复制到剪贴板函数
    def pic_ctrl_c(pathfile):
        img = Image.open(pathfile)
        output = BytesIO()  # 如是StringIO分引起TypeError: string argument expected, got 'bytes'
        img.convert("RGB").save(output, "BMP")  # 以BMP格式保存流
        data = output.getvalue()[14:]  # bmp文件头14个字节丢弃
        output.close()
        clipboard.OpenClipboard()  # 打开剪贴板
        clipboard.EmptyClipboard()  # 先清空剪贴板
        clipboard.SetClipboardData(win32con.CF_DIB, data)  # 将图片放入剪贴板
        clipboard.CloseClipboard()
        return


    # 查找QQ(TIM)窗口，发送人双击，激活为单独窗口
    title_name = '父愁者联盟'
    win = win32gui.FindWindow('TXGuiFoundation', title_name)
    print("找到句柄：%x" % win)
    if win != 0:
        left, top, right, bottom = win32gui.GetWindowRect(win)
        print(left, top, right, bottom)  # 最小化为负数,有时可以发
        win32gui.SetForegroundWindow(win)
    else:
        print('请注意：找不到【%s】这个人（或群），请激活窗口！' % title_name)
    #
    # #定义文本信息
    # msgs = ['就这就这', '小趴菜', '你们快睡觉', '这么快就不行了？', '这么晚了还不睡觉？', '你们加油我通宵']
    # str1 = random.choice(msgs)

    # 粘贴到发送区域
    pic_names = ['主动熬夜.jpg', '守夜冠军1.jpg', '守夜冠军2.jpg', '守夜冠军3.png', '守夜冠军4.jpg', ]
    ture_pic = random.choice(pic_names)
    input_file = str(ture_pic)  # 要发送的图片文件
    pic_ctrl_c(input_file)
    time.sleep(1)
    win32api.PostMessage(win, win32con.WM_PASTE, 0, 0)  # 相当于CTRL V
    # keyboard.type(str1)  # 发送字符串消息,需要pip install pynput
    time.sleep(1)  # 缓冲时间
    #
    # 如果QQ回车发送，以下单独回车
    # win32gui.SendMessage(win,win32con.WM_KEYDOWN,win32con.VK_RETURN,0)
    #
    # 以下为“CTRL+回车”组合键发送
    win32api.keybd_event(17, 0, 0, 0)  # 有效，按下CTRL
    time.sleep(1)  # 需要延时
    win32gui.SendMessage(win, win32con.WM_KEYDOWN, 13, 0)  # 窗口回车代码：win32con.VK_RETURN
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开CTRL
    #
    times = [1800, 1920, 1500, 2080, 1200, 2400]
    rightTime = random.choice(times)
    print("等待%d秒后再次发送" % rightTime)
    time.sleep(rightTime)
