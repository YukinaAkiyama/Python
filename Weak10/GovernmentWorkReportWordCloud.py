# 原课程中是政府工作报告词云
import jieba
import wordcloud
from imageio import imread

diymask = imread("五角星.png")
f = open("目光.txt", encoding='UTF-8')
t = f.read()
f.close()
ls = jieba.lcut(t)
ls = [i for i in ls if len(i) > 1]  # 去除单个字以及各类字符
txt = " ".join(ls)
w = wordcloud.WordCloud(
    font_path="msyh.ttc", mask=diymask, width=1000, height=700,
    background_color='white', max_words=20,
    stopwords={"这个", "可以", "我们", '他们', '很多', '什么', '一个', '没有', '就是', "一些", "所以", '他们', '一种'}
)
w.generate(txt)
w.to_file("grwordcloud.png")
