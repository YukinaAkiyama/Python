
dictionary = {"0": "零", "1": "壹", "2": "贰", "3": "叁", "4": "肆", "5": "伍", "6": "陆", "7": "柒", "8": "捌", "9": "玖"}
numbers = []
numbers2 = []

print("请输入十个数字：\n")
for i in range(10):
    a = input()
    if a == '':
        break
    numbers.append(a)

print("".join(numbers))

if numbers[0].isdigit():
    for i in numbers:
        numbers2.append(dictionary.get(i))

else:
    for i in numbers:
        for key, val in dictionary.items():
            if val == i:
                numbers2.append(key)
print("".join(numbers2))
