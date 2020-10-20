# coding=utf-8

# 鼠标坐标（x,y）的获取，以及绘制一条线，这条线的起点坐标在（0,0），另外一个端点随鼠标移动而移动
# 同时我们还要计算鼠标坐标与中心点的距离（运用勾股定理进行计算）

import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget)
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

class Example(QWidget):
    distance_from_center = 0
    def __init__(self):
        super().__init__()
        self.initUI()
        # 默认情况下禁用鼠标跟踪， 如果启用鼠标跟踪，即使没有按钮被按下，小部件也会接收鼠标移动事件。
        self.setMouseTracking(True)
    def initUI(self):
        self.setGeometry(200, 200, 1000, 500)
        self.setWindowTitle('标题')
        self.label = QLabel(self)
        self.label.resize(500, 40)
        self.show()
        self.pos = None

    def mouseMoveEvent(self, event):
        distance_from_center = round(((event.y() - 250)**2 + (event.x() - 500)**2)**0.5)
        # 这里设置了label的内容
        self.label.setText('坐标: ( x: %d ,y: %d )' % (event.x(), event.y()) + " 离中心点距离: " + str(distance_from_center))
        self.pos = event.pos()
        self.update()

    def paintEvent(self, event):
        if self.pos:
            q = QPainter(self)
            q.drawLine(0, 0, self.pos.x(), self.pos.y())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())