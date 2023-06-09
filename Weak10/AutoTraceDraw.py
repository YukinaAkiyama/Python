# AutoTraceDraw.py
"""
基本步骤：
步骤1：定义数据文件格式（接口）
步骤2：编写程序，根据文件接口解析参数绘制图形
步骤3：编制数据文件

数据格式：
例：300,1,144,0,1,0
行进距离，转向判断（0左1右），转向角度，RGB三通道颜色
"""

import turtle as t

t.title("自动轨迹绘制")
t.setup(800, 600, 0, 0)
t.pencolor("red")
t.pensize(5)

# 数据读取
datals = []
f = open("data.txt")
for line in f:
    line = line.replace("\n", "")
    datals.append(list(map(eval, line.split(","))))
f.close()

for i in range(len(datals)):
    t.pencolor(datals[i][3], datals[i][4], datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
