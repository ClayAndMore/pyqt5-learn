# coding:utf-8

""" 抽象按钮
QAbstractButton也就是说这是一个高度抽象的按钮类，以它为基础，所有的按钮都具备其父类的方法和属性
"""

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QMessageBox

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.resize(500,300)
        self.setWindowTitle('抽象按钮（QAbstractButton）')

        label1 = QLabel('密码输入区',self)
        label1.move(40, 40)
        label2 = QLabel('正确密码：麻',self)
        label2.move(40, 200)
        label3 = QLabel('你输入的密码：',self)
        label3.move(40, 220)

        self.label4 = QLabel('  ',self)
        self.label4.move(150,220)

        bt1 = QPushButton('芝',self)
        bt2 = QPushButton('麻',self)
        bt3 = QPushButton('开',self)
        bt4 = QPushButton('门',self)

        bt1.move(40, 80)
        bt2.move(120, 80)
        bt3.move(200, 80)
        bt4.move(280, 80)
        # 此属性保存按钮是否可被选中。默认情况下，该按钮是不可被选中的。
        # 即默认情况下按钮按下后是要弹起来的，设置后，就像点灯开关一样，要么开要么关
        bt1.setCheckable(True)
        bt2.setCheckable(True)
        bt3.setCheckable(True)
        bt4.setCheckable(True)

        # 是否启用排它性，autoExclusive是默认关闭的。
        # 如果启用了自动排它性，那么属于同一个父部件的可选中按钮就会表现得好像它们是相同按钮组一部分一样。
        # 在这个唯一按钮组中，任何时候只有一个按钮可以被选中；选中另一个按钮会自动取消之前选中过的按钮。此属性对属于其它按钮组的按钮没有影响。
        bt1.setAutoExclusive(True)
        bt2.setAutoExclusive(True)
        bt3.setAutoExclusive(True)
        bt4.setAutoExclusive(True)

        bt1.clicked.connect(self.setPassword)
        bt2.clicked.connect(self.setPassword)
        bt3.clicked.connect(self.setPassword)
        bt4.clicked.connect(self.setPassword)

        self.show()

    def setPassword(self):
        word = self.sender().text()
        self.label4.setText(word)
        if word == '麻':
            QMessageBox.information(self,'提示','恭喜，密码正确，可以进入！')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

""" 设立了9个按钮，分成了3组，每组中的按钮是互斥
self.btg1 = QButtonGroup(self)
self.btg2 = QButtonGroup(self)
self.btg3 = QButtonGroup(self)

self.btg1.addButton(self.bt11,1)
self.btg1.addButton(self.bt12,2)
self.btg1.addButton(self.bt13,3)
self.btg2.addButton(self.bt21,1)
self.btg2.addButton(self.bt22,2)
self.btg2.addButton(self.bt23,3)
self.btg3.addButton(self.bt31,1)
self.btg3.addButton(self.bt32,2)
self.btg3.addButton(self.bt33,3)

"""