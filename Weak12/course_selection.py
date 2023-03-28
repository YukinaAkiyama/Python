import sys
from PySide6.QtWidgets import (QApplication, QDialog, QVBoxLayout, QHBoxLayout, QRadioButton, QListWidget, QPushButton)
from PySide6.QtCore import Qt


class course(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("课程")

        self.courses = ["Python 程序设计", "数据结构", "计算机网络", "Java 程序设计"]

        self.course_list_remain = QListWidget()
        self.course_list_choose = QListWidget()
        self.confirm = QPushButton(">>")
        self.cancel = QPushButton("<<")

        for i in self.courses:
            self.course_list_remain.addItem(i)

        self.buttons = QVBoxLayout()
        self.buttons.addWidget(self.confirm)
        self.buttons.addWidget(self.cancel)

        self.confirm.setFixedWidth(50)
        self.cancel.setFixedWidth(50)

        self.main = QHBoxLayout()
        self.main.addWidget(self.course_list_remain)
        self.main.addLayout(self.buttons)
        self.main.addWidget(self.course_list_choose)

        self.setLayout(self.main)

        self.resize(300, 300)

        self.confirm.clicked.connect(self.f_confirm)
        self.cancel.clicked.connect(self.f_cancel)

    def f_confirm(self):
        for i in range(self.course_list_remain.count()):
            if self.course_list_remain.item(i).isSelected():
                self.course_list_choose.addItem(self.course_list_remain.item(i).text())
                self.course_list_remain.takeItem(i)
        pass

    def f_cancel(self):
        for i in range(self.course_list_choose.count()):
            if self.course_list_choose.item(i).isSelected():
                self.course_list_remain.addItem(self.course_list_choose.item(i).text())
                self.course_list_choose.takeItem(i)
        pass


if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    w = course()
    w.show()
    app.exec()
