import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    exfile = open('Top20.txt', 'w')
    print(exfile)
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:  #先检索到tbody标签
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')  #查询tr中的td标签，等价于tr.find_all('td')
             # 新版的排名封装在a标签中，所以这里需要具体到查找属性为'name-cn'的a标签并存储其字符串，即大学的中文名称
            a = tr('a','name-cn')
            ulist.append([tds[0].string.strip(),a[0].string.strip(),tds[2].text.strip(),tds[4].string.strip()])  # 使用二维列表存储信息
    exfile.write(str(ulist))
    exfile.close()


def printUnivList(ulist, num):
    print("{:^11}\t{:^7}\t{:^11}".format("排名","学校名称","总分"))	#取10/6/10位中间对齐
    for i in range(num):
        u = ulist[i]
        print("{:^11}\t{:^7}\t{:^11}".format(u[0], u[1], u[3]))


def main():
    uinfo = []
    url = "https://www.shanghairanking.cn/rankings/bcur/2022"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)  # 20 univ


main()
