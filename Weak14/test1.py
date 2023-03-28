# 百度搜索全代码
# 全代码
import requests

url = 'http://www.so.com/s'
keyword = 'Python'
kv = {'wd': keyword}
try:
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3878.400 QQBrowser/10.8.4518.400'}
    r = requests.get(url, headers=headers, params=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:2000])
except:
    print('爬取失败')
