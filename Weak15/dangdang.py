import re
import csv
import requests
import time
from lxml import etree


def get_encoding(url, headers=None):  # 一般每个网站自己的网页编码都是一致的,所以只需要搜索一次主页确定
    'To get website\'s encoding from tag<meta content=\'charset=\'UTF-8\'>'  # 从<meta>标签中获取
    res = requests.get(url, headers=headers)
    charset = re.search("charset=(.*?)>", res.text)
    if charset is not None:
        blocked = ['\'', ' ', '\"', '/']
        filter = [c for c in charset.group(1) if c not in blocked]
        return ''.join(filter)  # 修改res编码格式为源网页的格式,防止出现乱码
    else:
        return res.encoding  # 没有找到编码格式,返回res的默认编码


# 2018-10 前500的畅销书的书名 ,使用在线爬虫,思路和离线做了些修改
# 爬取25页书单页面,对每个书单页面保存详细页的页面(一一对应)
# 最后同时写入书单页的信息,每个列表保存一个信息和详细页的信息

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
}  # 设置headers
encoding = get_encoding('http://www.dangdang.com', headers)  # 获取主站编码

urls = ['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-month-2018-10-1-{}'.format(i) for i in
        range(1, 26)]

# 在线爬虫的准备
detail_url = []
rank = []
site = []
name = []
star = []
author = []
ISBN = []
if __name__ == '__main__':
    for i in range(24):  # 0~24 ->1~25
        res = requests.get(urls[i], headers)
        res.encoding = encoding
        selector = etree.HTML(res.text)
        booklist = selector.xpath('//ul[@class="bang_list clearfix bang_list_mode"]/li')
        book = [book for book in booklist]
        for i in range(len(book)):
            rank.append(book[i].xpath('div[1]/text()')[0])  # 排名
            site.append(book[i].xpath('div[2]/a/@href')[0])  # 购买/详细页面
            name.append(book[i].xpath('div[3]/a/text()')[0])  # 名字
            star.append(book[i].xpath('div[4]/span/span/@style'))  # 以星星宽度决定好评
            author.append(book[i].xpath('div[5]/a/text()'))  # 作者名
        time.sleep(0.5)
    for url in site:
        res = requests.get(url, headers)
        res.encoding = encoding
        pattern = '//ul[@class="bang_list clearfix bang_list_mode"]/li/div[2]/a/@href'
        ISBN.append(etree.HTML(res.text).xpath('//ul[@class="key clearfix"]/li[5]/text()')[0])  # 获取每一本书的详细页面
        time.sleep(0.5)
tmp = []
for s in star:
    tmp.append(''.join([c for c in str(s) if c.isdigit() or c == '.']))
star = tmp
rank = [r.replace('.', '') for r in rank]
author = [' '.join(a) for a in author]
ISBN = [i.replace('国际标准书号ISBN：', '') + '\t' for i in ISBN]
output = open('D:/Python项目/Weak15/result.csv', 'w', encoding=encoding, newline='')  # 将信息导出到csv,设置newline=""去除写一行空一行的影响
writer = csv.writer(output)  # csv writer
writer.writerow(('排名', '书名', '作者', '好评率', '购买页面', 'ISBN'))
for i in range(len(rank)):
    writer.writerow((rank[i], name[i], author[i], star[i], site[i], ISBN[i]))  # 保存到csv
