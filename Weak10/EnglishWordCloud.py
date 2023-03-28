# 应用实例1：英文词云
import wordcloud
txt = "life is shorted, you need python"
w = wordcloud.WordCloud(
    background_color = 'white')
w.generate(txt)
w.to_file("pywcloud.png")
