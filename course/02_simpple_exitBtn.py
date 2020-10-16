# coding:utf-8

# 单独声明类， 设置窗口图标, 退出按钮

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class Ico(QWidget):
    def __init__(self):
        super().__init__() # 要用QWidget中__init__的变量
        self.initUI()

    def initUI(self):
        #  setGeometry（）做了两件事情：它在屏幕上定位窗口并设置它的大小；前两个参数是窗口的x和y位置；第三个是宽度；第四个是窗口的高度。
        #  实际上，它在一个方法中组合了resize（）和move（）方法。
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('标题')
        self.setWindowIcon(QIcon('tubiao.ico'))

        btn = QPushButton("退出", self)
        """
        PyQt5中的事件处理系统采用信号和槽机制构建。 如果我们点击按钮，点击的信号被发出。 槽可以是Qt槽函数或任何Python可调用的函数。 
        QCoreApplication包含主事件循环; 它处理和调度所有事件。 instance（）方法给我们当前的实例。
        QCoreApplication是通过QApplication创建的。 点击的信号连接到终止应用程序的quit（）方法。
        """
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(70, 30)
        btn.move(50, 50)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ico()
    sys.exit(app.exec_())