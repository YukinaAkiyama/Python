from bs4 import BeautifulSoup
import requests

shop_name = input("请输入要爬取的商品名称: ")
url = "https://search.jd.com/Search?keyword=" + shop_name
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
# 设置请求头以免被发现是爬虫
htmldata = requests.get(url, headers=headers)  # 得到一个请求对象
htmldata = htmldata.text  # 获取html源码

soup = BeautifulSoup(htmldata, 'html.parser')  # 创建一个bs4对象
# 爬取图片
img_all = soup.find_all('img', attrs={"data-lazy-img": "done", "data-img": "1"})  # 搜索所有<img>标签，且属性值是done和1
get_img_data = []
num = 0  # 初始值
for i in img_all:
    if num >= 60:
        break
        # 只要前60张图片，因为前60张才是商品的图片，其他的都是广告
    get_img_data.append(i.get("src"))  # 将图片添加至数组
    num += 1

# 爬取标题
title_all = soup.find_all('div', attrs={"class": "p-name p-name-type-2"})
# 搜索所有<div>标签，且属性值是p-name p-name-type-2
get_title_data = []
for i in title_all:
    get_title_data.append(i.find_all("em")[0].text)  # 获取所有em,[0]是因为会返回一个数组

# 爬取价格
rmb_all = soup.find_all("strong", attrs={"data-presale": "0"})
get_rmb_data = []
for i in rmb_all:
    get_rmb_data.append(i.text.replace("￥", "").replace("\n", ""))  # 获取价格并且将￥去掉

# 爬取链接
url_all = soup.find_all("div", attrs={"class": "p-name p-name-type-2"})
get_url_data = []
for i in url_all:
    get_url_data.append(i.a.get("href"))

# 爬取店铺名称
name_all = soup.find_all("a", attrs={"class": "curr-shop hd-shopname"})
get_name_data = []
for i in name_all:
    get_name_data.append(i.text)

# 爬取评论数量
comment_num_all = soup.find_all("div", attrs={"class": "p-commit", "data-done": "1"})
get_comment_num_data = []
for i in comment_num_all:
    get_comment_num_data.append(i.a.text)

data = []  # 存储所有数据
for i in range(len(get_img_data)):
    temp = []  # 存储单个数据
    temp.append(get_img_data[i])
    temp.append(get_title_data[i])
    temp.append(get_rmb_data[i])
    temp.append(get_url_data[i])
    temp.append(get_name_data[i])
    temp.append(get_comment_num_data[i])
    data.append(temp)  # 存入所有数据
print(data)