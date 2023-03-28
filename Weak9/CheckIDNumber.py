import json
f = open("身份证号码归属地对照表.txt",'r',encoding='utf-8')
content = f.read()
content_dict = json.loads(content)
print(content_dict)
print(type(content_dict))
key = eval(input("输入身份证号码前六位："))
if key in content_dict.keys():
    print(content_dict[key])
else:
    print("没有该地址")