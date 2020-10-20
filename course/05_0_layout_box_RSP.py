#coding = 'utf-8'

# 剪刀石头布，箱式布局
# QHBoxLayout和QVBoxLayout是基本的布局类，它们在水平和垂直方向上排列小部件。

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QHBoxLayout, QVBoxLayout)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()

    def Init_UI(self):
        self.setGeometry(300,300,400,300)
        self.setWindowTitle('标题')

        bt1 = QPushButton('剪刀', self)
        bt2 = QPushButton('石头', self)
        bt3 = QPushButton('布', self)

        # 我们创建一个水平框布局，并添加一个拉伸因子和三个按钮。
        # 这个拉伸在三个按钮之前增加了一个可伸缩的空间。这将把它们推到窗口的右边。
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(bt1)
        hbox.addWidget(bt2)
        hbox.addWidget(bt3)


        vbox = QVBoxLayout() # 创建垂直布局
        vbox.addStretch(1)   # 垂直框中的拉伸因子将按钮的水平框推到窗口的底部。
        vbox.addLayout(hbox) # 水平布局放置在垂直布局中。

        self.setLayout(vbox) # 最后设置窗口的主要布局

        self.show()

"""
addStretch函数的作用是在布局器中增加一个伸缩量
        hbox = QHBoxLayout()
        hbox.addStretch(1) #增加伸缩量
        hbox.addWidget(bt1)
        hbox.addStretch(1)#增加伸缩量
        hbox.addWidget(bt2)
        hbox.addStretch(1)#增加伸缩量
        hbox.addWidget(bt3)
        hbox.addStretch(6)#增加伸缩量
其中四个addStretch()函数用于在button按钮间增加伸缩量，
伸缩量的比例为1:1:1:6，意思就是将button以外的空白地方按设定的比例等分为9份并按照设定的顺序放入布局器中。

| 1 | 剪刀 | 1 | 石头 | 1 | 布 |    6    | 
"""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())