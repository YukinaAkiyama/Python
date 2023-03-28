list1 = [12, 23, 34, 45, 56, 67, 78]
list2 = [13, 35, 57, 79, 56, 67]

for key1 in list1:
    for key2 in list2:
        if key1 == key2:
            print('same:', key1)
