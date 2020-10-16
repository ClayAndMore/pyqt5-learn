# coding:utf-8

# 一个最简单的pyqt程序

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if  __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget() # QWidget小部件是PyQt5中所有用户界面对象的基类。
    w.resize(250, 150) # resize（）方法调整窗口小部件的大小。这里我们设定窗口的大小：宽250像素，高150像素。
    w.move(300, 300)  # move（）方法将小部件移动到屏幕上x = 300，y = 300坐标处的位置. 屏幕坐标是从屏幕左上角开始算的
    w.setWindowTitle("窗口标题")
    w.show()

    sys.exit(app.exec())