# coding:utf-8

# 简单的信号与槽示例
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QDial, QApplication, QSlider)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        lcd = QLCDNumber(self)
        slider = QSlider(self)
        # dial = QDial(self)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('标题')

        lcd.setGeometry(100,50,150,60)
        # dial.setGeometry(120,120,100,100)
        slider.setGeometry(120,120,100,50)

        # dial.valueChanged.connect(lcd.display)
        slider.valueChanged.connect(lcd.display)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())