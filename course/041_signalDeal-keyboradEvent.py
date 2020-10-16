#coding=utf-8

# 方向按键事件处理

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
    def initUi(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('标题')

        self.lab = QLabel('方向',self)

        self.lab.setGeometry(150,100,50,50)

        self.show()

    # 重新实现了keyPressEvent（）事件处理程序
    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Up:
            self.lab.setText('↑')
        elif e.key() == Qt.Key_Down:
            self.lab.setText('↓')
        elif e.key() == Qt.Key_Left:
            self.lab.setText('←')
        else:
            self.lab.setText('→')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())