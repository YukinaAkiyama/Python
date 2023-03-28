with open("content.text", "r", encoding="UTF-8") as f:
    text = f.read()

new_text = text.split("\n")

for item in new_text:
    count = 0
    for i in range(len(item)):
        if item[i] == '.':
            count += 1
    with open("new_content.text", "a", encoding="UTF-8") as f:
        f.write((count * " ") + item + "\n")