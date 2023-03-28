import jieba

txt = open('红楼梦.txt', 'r', encoding='utf-8').read()

words = jieba.lcut(txt)

counts = {}

names = ['贾母', '老太太', '尤氏', '贾珍', '贾蓉', '秦可卿', '贾赦', '邢夫人', '贾政',
         '王夫人', '袭人', '蕊珠', '贾琏', '王熙凤', '紫鹃', '鹦哥', '香菱', '甄英莲',
         '薛蟠', '夏金桂', '贾宝玉', '宝玉', '林黛玉', '黛玉', '林姑娘', '林妹妹',
         '凤姐', '刘姥姥', '晴雯', '', '', '', '']

for word in words:
    if len(word) == 1:
        continue
    elif word == '贾母' or word == '老太太':
        word = '贾母'
    elif word == '尤氏' or word == '贾珍':
        word = '贾珍'
    elif word == '贾蓉' or word == '秦可卿':
        word = '贾蓉'
    elif word == '贾赦' or word == '邢夫人':
        word = '贾赦'
    elif word == '贾政' or word == '王夫人':
        word = '贾政'
    elif word == '袭人' or word == '蕊珠':
        word = '袭人'
    elif word == '贾琏' or word == '王熙凤' or word == '凤姐':
        word = '贾琏'
    elif word == '紫鹃' or word == '鹦哥':
        word = '紫鹃'
    elif word == '香菱' or word == '甄英莲':
        word = '香菱'
    elif word == '晴雯':
        word = '晴雯'
    elif word == '薛蟠' or word == '夏金桂':
        word = '薛蟠'
    elif word == '贾宝玉' or word == '宝玉':
        word = '贾宝玉'
    elif word == '林黛玉' or word == '林姑娘' or word == '林妹妹' or word == '黛玉':
        word = '林黛玉'
    elif word == '刘姥姥':
        word = '刘姥姥'
    if word not in names:
        continue
    counts[word] = counts.get(word, 0) + 1

items = list(counts.items())

items.sort(key=lambda x: x[1], reverse=True)

print('出现次数最多的是:', items[0][0], '出现了：', items[0][1], '次')
for item in items:
    print(item[0], '出现了：', item[1], '次')
