import requests
from bs4 import BeautifulSoup

req = requests.get(url="https://python123.io/ws/demo.html")
req.encoding = "utf-8"
html = req.text
soup = BeautifulSoup(req.text, features="html.parser")

print("一小题：\n名称：", soup.a.name,
      "\n属性：", soup.a.attrs,
      "\n文字内容：", soup.a.string)

print("\n二小题：")
for child in soup.body.contents:
    if str(child.name) != 'None':
        print("每个子孙标签：", str(child.name))

print("\n三小题：")
for child in soup.body.children:
    if str(child.name) != 'None':
        print("每个子孙标签：", str(child.name))

print("\n四小题：")
for child in soup.html.descendants:
    if str(child.name) != 'None':
        print("每个子孙标签：", str(child.name))

print("\n五小题：")
for target in soup.find_all('a'):
    try:
        value = target.get('href')
    except:
        value = ''
    if value:
        print(value)

print("\n六小题：")
# for sibling in soup.a.previous_sibling:
#     print(sibling)
