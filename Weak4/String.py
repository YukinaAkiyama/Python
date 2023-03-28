str_1 = input("输入字符串:")
print("输入的是:", str_1)
uppercase = 0
lowercase = 0
numbers = 0
spaces = 0
others = 0
for i in range(len(str_1)):
    if 'A' <= str_1[i] <= 'Z':
        uppercase += 1
    elif 'a' <= str_1[i] <= 'z':
        lowercase += 1
    elif '0' <= str_1[i] <= '9':
        numbers += 1
    elif str_1[i] == ' ':
        spaces += 1
    else:
        others += 1

print("uppercase:", uppercase,
      "\nlowercase:", lowercase,
      "\nnumbers:", numbers,
      "\nspaces:", spaces,
      "\nothers:", others)
