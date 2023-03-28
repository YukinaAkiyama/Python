# 从 CSV 格式的文件中读入数据
fo = open("f_deal.txt")
ls_1 = []
for line in fo:
    line = line.replace("\n","")
    ls_1.append(line.split(","))
fo.close()

# 将数据写入 CSV 格式的文件
ls_2 = [['China','CN'],['American','USA'],['Japan','JPN']]
fw = open("f_deal.txt","w")
for item in ls_2:
    fw.write(','.join(item)+'\n')
fw.close()
