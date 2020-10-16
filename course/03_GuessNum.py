# coding:utf-8

# QLineEdit, QMessageBox 的使用
# 自定义关闭事件

import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon

class GuessNum(QWidget):
    def __init__(self):
        super(GuessNum, self).__init__()
        self.initUI()
        self.num = randint(1, 100)

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('猜数字')
        self.setWindowIcon(QIcon('tubiao.ico'))

        self.text = QLineEdit("在这里输入数字", self)
        self.text.selectAll()
        self.text.setFocus()
        self.text.setGeometry(80, 50, 150 ,30)

        self.bt1 = QPushButton("guess", self)
        self.bt1.setGeometry(115, 150, 70 ,30)
        # setToolTip 可以让鼠标悬停在按钮上出现文本，这里使用了富文本
        self.bt1.setToolTip('<b>点击这里猜数字</b>')
        self.bt1.clicked.connect(self.showMessage)

        self.show()

    def showMessage(self):
        guess_num = int(self.text.text())
        print(self.num)

        # QMessageBox除了有about外，还有我们程序中用到的QMessageBox.question,
        # 还有QMessageBox.critical, QMessageBox.warning， QMessageBox.information，它们只是图标不一样。

        if guess_num > self.num:
            QMessageBox.about(self, '看结果', '猜大了!')
            self.text.setFocus()
        elif guess_num < self.num:
            QMessageBox.about(self, '看结果', '猜小了!')
            self.text.setFocus()
        else:
            QMessageBox.about(self, '看结果', '答对了!进入下一轮!')
            self.num = randint(1, 100)
            self.text.clear()
            self.text.setFocus()

    # 如果关闭QWidget，则生成QCloseEvent。 要修改widget的行为，我们需要重新实现closeEvent（）事件处理程序。
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = GuessNum()
    sys.exit(app.exec_())