import requests
from bs4 import BeautifulSoup

req = requests.get(url="https://python123.io/ws/demo.html")
req.encoding = "utf-8"
html = req.text
soup = BeautifulSoup(req.text, features="html.parser")

print("一小题：\n名称：", soup.a.name,
      "\n属性：", soup.a.attrs,
      "\n文字内容：", soup.a.string)

print("\n二小题：\n", soup.body.contents)

print("\n三小题：")
for child in soup.body.descendants:
    print("每个子孙标签：", str(child))

print("\n四小题：")
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

print("\n五小题：")
for sibling in soup.a.next_sibling:
    print(sibling)

print("\n六小题：")
for sibling in soup.a.previous_sibling:
    print(sibling)
