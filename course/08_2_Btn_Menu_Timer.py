#coding: utf-8

"""
菜单按钮
倒计时按钮
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt5.QtCore import QTimer

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 150)

        self.bt1 = QPushButton("这是什么", self)
        self.bt1.move(40, 40)

        self.bt2 = QPushButton('发送验证码', self)
        self.bt2.move(150, 40)

        # 创建一个菜单
        menu = QMenu(self)
        menu.addAction('我是')
        menu.addSeparator()
        menu.addAction('世界上')
        menu.addSeparator()  # 添加分割符
        menu.addAction('最帅的')

        # 把菜单添加到按钮
        self.bt1.setMenu(menu)

        self.count = 10

        self.bt2.clicked.connect(self.Action)

        # 创建一个QTimer，将其timeout()信号连接到相应的插槽，然后调用start()。
        # 从此以后，它将以固定的时间间隔发出timeout()信号。
        self.time = QTimer(self)
        # 设置间隔为1s
        self.time.setInterval(1000)
        self.time.timeout.connect(self.Refresh)

        self.show()

    def Action(self):
        if self.bt2.isEnabled():
            self.time.start()
            self.bt2.setEnabled(False)

    def Refresh(self):
        if self.count > 0:
            self.bt2.setText(str(self.count ) +'秒后重发')
            self.count -= 1
        else:
            self.time.stop()
            self.bt2.setEnabled(True)
            self.bt2.setText('发送验证码')
            self.count = 10

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())