class WordsBook:
    def __init__(self):
        self.words = []

    @staticmethod
    def welcome():
        print('*' * 20)
        print("！！欢迎使用单词表！！\n",
              "1.添加单词\n",
              "2.查看单词本\n",
              "3.删除单词\n",
              "4.背单词\n",
              "5.清空单词表\n",
              "6.退出\n",
              '*' * 20)

    def addNewWord(self):
        word_id = input('编号:')
        name = input('单词: ')
        paraphrase = input('释义: ')
        level = input('熟悉程度:')

        word = {'id': word_id, 'name': name, 'paraphrase': paraphrase, 'level': level}
        self.words.append(word)

    def listWord(self):
        for word in self.words:
            print(' 编  号:%s\n' % (word['id']),
                  '单   词:%s\n' % (word['name']),
                  '释   义:%s\n' % (word['paraphrase']),
                  '熟悉程度:%s\n' % (word['level']))

    def reciteWord(self):
        name = input('单词: ')
        for word in self.words:
            if word['name'] == name:
                print(' 编  号:%s\n' % (word['id']),
                      '单   词:%s\n' % (word['name']),
                      '释   义:%s\n' % (word['paraphrase']),
                      '熟悉程度:%s\n' % (word['level']))

    def deleteWord(self):
        name = input('单词: ')
        for word in self.words:
            if word['name'] == name:
                self.words.remove(word)
                break

    def clearWord(self):
        self.words.clear()

    def getChoice(self):
        choice = int(input("请选择："))
        if choice == 1:
            self.addNewWord()
        elif choice == 2:
            self.listWord()
        elif choice == 3:
            self.deleteWord()
        elif choice == 4:
            self.reciteWord()
        elif choice == 5:
            self.clearWord()
        elif choice == 6:
            exit()
        else:
            print('Invalid choice!')


if __name__ == '__main__':
    wordsBook = WordsBook()
    while True:
        wordsBook.welcome()
        wordsBook.getChoice()
