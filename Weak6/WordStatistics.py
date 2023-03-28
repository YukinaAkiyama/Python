with open('words.txt', encoding='utf-8') as file_obj:
    contents = file_obj.read()

words = dict(map(lambda x: (x, contents.split().count(x)), contents.split()))
sorted_words = sorted(words.items(), key=lambda x: x[1], reverse=True)
count = 0
Top_10 = {}
for k, v in sorted_words:
    if count < 10:
        Top_10[k] = v
        count += 1
    else:
        break

print(Top_10)
