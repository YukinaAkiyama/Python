import tkinter as tk
import tkinter.messagebox
import tkinter.ttk
from tkinter import *
import time
from datetime import datetime


from PIL import Image, ImageSequence, ImageTk

import function.GetMessage as gm
import function.Navigation as navi

# 窗口
window = tk.Tk()
window.title('公交车管理系统')
window.geometry('1120x840')


# 界面
def display_top():
    print('hello')
    # 地图
    tk.Label(window, text='地图').place(x=5, y=5)
    img = tkinter.PhotoImage(file="D:\\Python项目\\CourseDesign-Bus\\pic\\地图终版.png")
    map_label = tk.ttk.Label
    map_label(window, image=img).place(x=30, y=40)

    # -------------------------------------------------------
    # ===============================================================================
    # 信息查询函数
    def infoSearch():
        tl_infoSearch.delete(1.0, "end")
        # str_output = str(var_search.get())
        info = gm.GetStationMessage(str(var_search.get()))
        time = info[0]
        route = info[1]
        str_output = f"发车时间: \n{time}\n\n经过路线：\n{route}"
        tl_infoSearch.insert('insert', str_output)

    # 信息查询
    tk.ttk.Label(window, text='信息查询').place(x=610, y=30)
    tk.ttk.Label(window, text='选择站点').place(x=610, y=60)
    global var_search
    var_search = tk.StringVar()
    station_name_box = tkinter.ttk.Combobox(window, textvariable=var_search, width=16)
    station_name_box['value'] = ('菜市场', '中心小学', '医院', '购物中心', '政府', '长途车站', '幸福小区', '荷花镇', '加油站', '桃花镇')
    station_name_box.place(x=700, y=60)

    # 查询按钮
    bt_infoSearch = tk.ttk.Button(window, text='查询站点信息', command=lambda: infoSearch())
    bt_infoSearch.place(x=610, y=90)
    # 文本框
    tl_infoSearch = tk.Text(window, width=33, height=12)
    tl_infoSearch.place(x=600, y=130)

    # ----------------------------------------------
    # ===============================================================================
    # 最近站点函数
    def nearStation():
        tl_nearStation.delete(1.0, "end")
        # print("ceshi1")
        info = gm.NearestStation(str(pos_input.get()))
        # print("-------")
        station = info[0]
        time = info[1]
        route = info[2]
        str_output = f"最近站点：\n{station} \n\n发车时间: \n{time}\n\n经过路线：\n{route}"
        # print(type(info))

        # print("ceshi2")

        tl_nearStation.insert('insert', str_output)
        # print("ceshi3")

    # 最近站点
    tk.ttk.Label(window, text='最近站点').place(x=880, y=30)
    tk.ttk.Label(window, text='位置坐标').place(x=880, y=60)
    # 坐标输入框
    # global pos_input
    global pos_input
    pos_input = tk.StringVar()
    entry_pos_input = tk.ttk.Entry(window, textvariable=pos_input)
    entry_pos_input.place(x=960, y=60)
    # 查询按钮
    bt_nearStation = tk.ttk.Button(window, text='查询最近站点', command=lambda: nearStation())
    bt_nearStation.place(x=880, y=90)
    # 文本框
    tl_nearStation = tk.Text(window, width=33, height=12)
    tl_nearStation.place(x=870, y=130)

    # --------------------------------------------------------
    # ===============================================================================
    # 发车时间函数
    def busTime():
        tl_busTime.delete(1.0, "end")
        # str_output = str(var_search.get())
        info = gm.GetDownTime(str(date_str.get()), str(var_search1.get()))
        start_time = info[0]
        last_time_before = info[1]
        last_time_after = info[2]
        str_output = f"该站点发车时间: \n{start_time}\n\n最近一班车时间：\n{last_time_before}:{last_time_after}"
        tl_busTime.insert('insert', str_output)

    # 近期发车时间
    tk.ttk.Label(window, text='近期发车时间').place(x=610, y=315)
    # 时间选择
    tk.ttk.Label(window, text='选择时间').place(x=610, y=350)
    global date_str
    date_str = tk.StringVar()
    date = tk.ttk.Entry(window, textvariable=date_str, width=19)
    date.place(x=700, y=350)
    date_str.set(datetime.now().strftime("%H:%M"))
    # 站点选择
    tk.ttk.Label(window, text='选择站点').place(x=610, y=390)
    # combox
    global var_search1
    var_search1 = tk.StringVar()
    station_name_box1 = tkinter.ttk.Combobox(window, textvariable=var_search1, width=16)
    station_name_box1['value'] = ('菜市场', '中心小学', '医院', '购物中心', '政府', '长途车站', '幸福小区', '荷花镇', '加油站', '桃花镇')
    station_name_box1.place(x=700, y=390)
    # 查询按钮
    bt_nearStation = tk.ttk.Button(window, text='查询最近站点', command=lambda: busTime())
    bt_nearStation.place(x=610, y=435)
    # 文本框
    tl_busTime = tk.Text(window, width=33, height=12)
    tl_busTime.place(x=870, y=305)

    # -------------------------------------------------------
    # ===============================================================================
    # 导航函数
    def navigation():
        tl_navigation.delete(1.0, "end")
        # str_output = str(var_search.get())
        info = navi.Navigation(str(var_search2.get()), str(var_search3.get()))
        print(info)
        # start_station = info[0]
        # stop_station = info[1]
        # end_station = info[2]
        str_output = f"最优路线: \n{info}"
        tl_navigation.insert('insert', str_output)

    # 导航界面
    tk.ttk.Label(window, text='导航').place(x=30, y=490)
    # 时间选择
    tk.ttk.Label(window, text='选择站点站').place(x=30, y=525)
    # combox
    global var_search2
    var_search2 = tk.StringVar()
    station_name_box2 = tkinter.ttk.Combobox(window, textvariable=var_search2, width=16)
    station_name_box2['value'] = ('菜市场', '中心小学', '医院', '购物中心', '政府', '长途车站', '幸福小区', '荷花镇', '加油站', '桃花镇')
    station_name_box2.place(x=155, y=525)
    # 站点选择
    tk.ttk.Label(window, text='选择终点站').place(x=30, y=567)
    # combox
    global var_search3
    var_search3 = tk.StringVar()
    station_name_box3 = tkinter.ttk.Combobox(window, textvariable=var_search3, width=16)
    station_name_box3['value'] = ('菜市场', '中心小学', '医院', '购物中心', '政府', '长途车站', '幸福小区', '荷花镇', '加油站', '桃花镇')
    station_name_box3.place(x=155, y=567)
    # 查询按钮
    bt_nearStation = tk.ttk.Button(window, text='查询路线', command=lambda: navigation())
    bt_nearStation.place(x=140, y=607)
    # 文本框
    tl_navigation = tk.Text(window, width=37, height=12)
    tl_navigation.place(x=30, y=660)

    # 动态
    tk.ttk.Label(window, text='动态').place(x=340, y=490)
    #
    # map_label2 = tk.ttk.Label
    # map_label2(window).place(x=370, y=510)

    canvas = tk.Canvas(window, width=730, height=310, bg='white')
    canvas.place(x=370, y=510)

    # 分解gif并逐帧显示
    def pick(event):
        global a, flag
        while 1:
            im = Image.open('D:\\Python项目\\CourseDesign-Bus\\pic\\开摆.gif')
            # GIF图片流的迭代器
            iter = ImageSequence.Iterator(im)
            # frame就是gif的每一帧，转换一下格式就能显示了
            for frame in iter:
                pic = ImageTk.PhotoImage(frame)
                canvas.create_image((367, 157), image=pic)
                time.sleep(0.01)
                window.update_idletasks()  # 刷新
                window.update()

    canvas.bind("<Enter>", pick)  # 这个事件是鼠标进入组件，用什么事件不重要，这里只是演示

    window.mainloop()


if __name__ == '__main__':
    display_top()
