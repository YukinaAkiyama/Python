print("欢迎使用好友管理系统！！\n"
      "1.添加好友\n"
      "2.删除好友\n"
      "3.备注好友\n"
      "4.展示好友\n"
      "5.退出程序")
friends: list = []
while True:
    choice = int(input())
    if choice == 1:
        print("请输入要添加的好友：")
        new_friend = str(input())
        friends.append(new_friend)

    elif choice == 2:
        print("请输入要删除的好友：")
        delete_friend = str(input())
        friends.remove(delete_friend)
        print("删除成功")

    elif choice == 3:
        print("请输入要修改的好友：")
        change_friend = str(input())
        print(change_friend)
        for i in friends:
            if friends[i] == change_friend:
                after_name = str(input("要修改为："))
                friends[i] = after_name
                print("修改成功!")

    elif choice == 4:
        if friends is None:
            print("还未添加过好友，列表为空!")
        else:
            print(friends)

    elif choice == 5:
        exit()

    print("1.添加好友\n"
          "2.删除好友\n"
          "3.备注好友\n"
          "4.展示好友\n"
          "5.退出程序")
