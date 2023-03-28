import jieba


# 获得去除标点的文本
def get_text(filename):
    with open(filename, 'r', encoding='utf-8') as fr:
        chinese = fr.read()
        # 要删除的标点
        del_ch = ['《', '，', '》', '\n', '。', '、', '；', '"', '：', ',', '！', '？', ' ']
        for ch in del_ch:
            chinese = chinese.replace(ch, '')  # 这里无需替换成空格
        return chinese


# 文件名改为要分析的文件
file_name = '三国.txt'
text = get_text(file_name)
vList = jieba.lcut(text)  # 调用jieba实现分词，返回列表

res_dict = {}
exclude = ['却说', '不能', '如何', '左右', '二人', '不可', '荆州', '如此', '商议', '主公', '军士']
# 进行词频统计
for i in vList:
    if len(i) <= 1:
        continue
    elif i in exclude:
        continue
    elif i == '玄德曰':
        ri = '玄德'
    elif i == '孔明曰':
        ri = '诸葛亮'
    elif i == '孔明':
        ri = '诸葛亮'
    elif i == '孟德曰':
        ri = '曹操'
    else:
        ri = i
    res_dict[ri] = res_dict.get(ri, 0) + 1
res_list = list(res_dict.items())
# 降序排序
res_list.sort(key=lambda x: x[1], reverse=True)

for i in range(10):
    word, count = res_list[i]
    pstr = str(i + 1) + ':'
    print(pstr, end=' ')
    print(word, count)
