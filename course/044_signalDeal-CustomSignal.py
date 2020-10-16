# coding=utf-8
# 发出自定义信号

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
from PyQt5.QtCore import (pyqtSignal, QObject)


class Signal(QObject):
    showmouse = pyqtSignal()  # 使用pyqtSignal创建一个新信号


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('学点编程吧')

        self.s = Signal()
        # 自定义showmouse信号连接到QMainWindow的about（）的槽。
        self.s.showmouse.connect(self.about)

        self.show()

    def about(self):
        QMessageBox.about(self,'鼠标','你点鼠标了吧！')

    def mousePressEvent(self, e):  # 按下鼠标事件， ps: emit() 这里是触发信号？待考证
        self.s.showmouse.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())