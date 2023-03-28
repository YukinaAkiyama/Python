class DialHistory:
    def __init__(self):
        self.persons = []

    @staticmethod
    def welcome():
        print('*' * 20)
        print("！！欢迎使用通讯录！！\n",
              "1.添加一个联系人\n",
              "2.查看所有联系人\n",
              "3.删除指定联系人\n",
              "4.修改联系人信息\n",
              "5.查找指定联系人\n",
              "6.退出\n",
              '*' * 20)

    def createPerson(self):
        personid = input('id:')
        name = input('name: ')
        phone = input('phone: ')
        email = input('email:')
        address = input('address: ')

        person = {'id': personid, 'name': name, 'phone': phone, 'email': email, 'address': address, }
        self.persons.append(person)

    def listPerson(self):
        for person in self.persons:
            print(' id:%s\n' % (person['id']),
                  'name:%s\n' % (person['name']),
                  'phone:%s\n' % (person['phone']),
                  'email:%s\n' % (person['email']),
                  'address:%s\n' % (person['address']))

    def queryPerson(self):
        name = input('name: ')
        for person in self.persons:
            if person['name'] == name:
                print(' id:%s\n' % (person['id']),
                      'name:%s\n' % (person['name']),
                      'phone:%s\n' % (person['phone']),
                      'email:%s\n' % (person['email']),
                      'address:%s\n' % (person['address']))

    def deletePerson(self):
        name = input('name: ')
        for person in self.persons:
            if person['name'] == name:
                self.persons.remove(person)
                break

    def changePerson(self):
        name = input('name: ')
        for person in self.persons:
            if person['name'] == name:
                self.persons.remove(person)
                print("new information:")
                personid = input('id:')
                name = input('name: ')
                phone = input('phone: ')
                email = input('email:')
                address = input('address: ')
                person = {'id': personid, 'name': name, 'phone': phone, 'email': email, 'address': address, }
                self.persons.append(person)

    def getChoice(self):
        choice = int(input("请选择："))
        if choice == 1:
            self.createPerson()
        elif choice == 2:
            self.listPerson()
        elif choice == 3:
            self.deletePerson()
        elif choice == 4:
            self.changePerson()
        elif choice == 5:
            self.queryPerson()
        elif choice == 6:
            exit()
        else:
            print('Invalid choice!')


if __name__ == '__main__':
    dialHistory = DialHistory()
    while True:
        dialHistory.welcome()
        dialHistory.getChoice()