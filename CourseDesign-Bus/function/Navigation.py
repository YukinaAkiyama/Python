def Navigation(start, end):
    dict1 = {1: "菜市场", 2: "中心小学", 3: "加油站", 4: "医院", 5: "幸福小区",
             6: "长途车站", 7: "购物中心", 8: "桃花镇", 9: "荷花镇", 10: "长途车站"}
    m = float('inf')
    for k, v in dict1.items():
        if v == start:
            a = k
    for k, v in dict1.items():
        if v == end:
            b = k
    c, d = a - 1, b - 1
    r = [
        [0, 2, m, m, 3, m, m, m, m, m],
        [2, 0, m, 2, m, m, m, m, m, m],
        [m, m, 0, 4, m, m, m, 3, m, m],
        [m, 2, 4, 0, m, m, 1, m, 1, m],
        [3, m, m, m, 0, m, m, m, m, 3],
        [m, m, m, m, m, 0, 1, m, m, m],
        [m, m, m, 1, m, 1, 0, m, m, 2],
        [m, m, 3, m, m, m, m, 0, m, m],
        [m, m, m, 1, m, m, m, m, 0, m],
        [m, m, m, m, 3, m, 2, m, m, 0]
    ]

    path = [[0 for i in range(10)] for j in range(10)]

    for i in range(10):
        for j in range(10):
            if r[i][j] != 0 and r[i][j] != m:
                path[i][j] = j

    for x in range(10):
        for i in range(10):
            for j in range(10):
                if r[i][x] + r[x][j] < r[i][j]:
                    r[i][j] = r[i][x] + r[x][j]
                    path[i][j] = path[i][x]

    print('最佳路径为：')
    global station_list
    station_list = []

    print(f'{dict1[c + 1]}→', end=' ')
    station_list.append(dict1[c + 1])

    while True:
        if path[c][d] == d:
            break
        print(f'{dict1[path[c][d] + 1]}→', end=' ')
        station_list.append(dict1[path[c][d] + 1])
        c = path[c][d]

    print(dict1[path[c][d] + 1])
    station_list.append(dict1[path[c][d] + 1])
    # print("\n1111111\n",station_list)

    return station_list

if __name__ == '__main__':
    Navigation("菜市场", "购物中心")
