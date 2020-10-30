# coding:utf-8

""" Qlabel 可以包含以下内容类型：

* 纯文本： 将字符串传递给setText()
* 富文本： 将富文本传递给setText()
* 图像：  将QPixmap对象传递给setPixmap()
* 动画:   将QMovie对象传递给setMovie()
* 数字：  将int或double数字传递给setNum(), 将数字转换为纯文本
* 空：    与纯文本相同，这是默认的，由clear()设置。

当在QLabel中使用setText()设置文本内容的时候，因为QLabel会尝试猜测它是将文本显示为纯文本还是作为HTML 4标记的一部分的富文本。
想明确地显示文本格式，请调用setTextFormat()
"""

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QRadioButton, QButtonGroup, QInputDialog, QApplication
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 400)

        self.lb1 = QLabel('我从春天里来，而你恰好也在！', self)
        self.lb1.setGeometry(10, 30, 500, 10)
        self.lb2 = QLabel('我内容很少哦1...', self)
        self.lb2.setGeometry(10, 80, 100, 20)
        self.lb3 = QLabel('我内容很少哦2...', self)
        self.lb3.setGeometry(10, 130, 100, 20)
        self.lb3.setWordWrap(True) # 当QLabel内容较多的时候，里面的内容可以换行, 实现自动换行

        self.bt1 = QPushButton('输入内容1', self)
        self.bt1.move(30, 100)
        self.bt2 = QPushButton('输入内容2', self)
        self.bt2.move(30, 150)

        self.ra1 = QRadioButton('左边', self)
        self.ra1.move(30, 50)
        self.ra2 = QRadioButton('中间', self)
        self.ra2.move(90, 50)
        self.ra3 = QRadioButton('右边', self)
        self.ra3.move(150, 50)

        self.bg1 = QButtonGroup(self)
        self.bg1.addButton(self.ra1, 1)
        self.bg1.addButton(self.ra2, 2)
        self.bg1.addButton(self.ra3, 3)

        self.bg1.buttonClicked.connect(self.rbclicked)
        self.bt1.clicked.connect(self.showDialog)
        self.bt2.clicked.connect(self.showDialog)

        self.show()

    def rbclicked(self):
        if self.bg1.checkedId() == 1:
            self.lb1.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        elif self.bg1.checkedId() == 2:
            self.lb1.setAlignment(Qt.AlignCenter)
        elif self.bg1.checkedId() == 3:
            self.lb1.setAlignment(Qt.AlignVCenter | Qt.AlignRight)

    def showDialog(self):
        sender = self.sender()
        if sender == self.bt1:
            text, ok = QInputDialog.getText(self, '内容1', '请输入内容1：')
            if ok:
                self.lb2.setText(text)
        elif sender == self.bt2:
            text, ok = QInputDialog.getText(self, '内容2', '请输入内容2：')
            if ok:
                self.lb3.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())