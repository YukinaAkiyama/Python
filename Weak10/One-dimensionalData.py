# 从空格分隔的文件中读入数据
txt = open("f_deal").read()
ls_1 = txt.split()

# 从特殊符号分隔的文件中读入数据
txt = open("f_deal").read()
ls_2 = txt.split("$")

# 采用空格分隔方式将数据写入文件
ls = ['中国','美国','日本']
f = open("f_deal.txt",'w')
f.write(''.join(ls))
f.close()

# 采用特殊分隔方式将数据写入文件
ls = ['中国','美国','日本']
f = open("f_deal.txt",'w')
f.write(''.join(ls))
f.close()
