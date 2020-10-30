# coding=utf-8

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtGui import QMovie, QPixmap
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.resize(550, 300)
        self.setWindowTitle('标签:动画（QLabel）')

        self.lb = QLabel(self)
        self.lb.setGeometry(100, 50, 300, 200)

        self.bt1 = QPushButton('开始', self)
        self.bt2 = QPushButton('停止', self)

        self.bt1.move(100, 20)
        self.bt2.move(280, 20)

        self.pix = QPixmap('movie.gif')
        self.lb.setPixmap(self.pix)
        self.lb.setScaledContents(True)  # 之前说过，填充空间

        self.bt1.clicked.connect(self.run)
        self.bt2.clicked.connect(self.run)

        self.show()

    def run(self):
        movie = QMovie("movie.gif")
        self.lb.setMovie(movie)
        if self.sender() == self.bt1:
            movie.start()
        else:
            movie.stop()
            self.lb.setPixmap(self.pix)

    """ QMovie类是用QImageReader播放动画的便捷类。
    这个类用来显示没有声音的简单的动画。如果您要显示视频和媒体内容，请改为使用Qt多媒体多媒体框架。
    """


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


"""
每当电影中有新的帧时，QMovie将发出updated()信号。如果框架的大小发生变化，则发出resized()信号。
您可以调用currentImage()或currentPixmap()来获取当前帧的副本。当电影完成后，QMovie发出finished()。
如果播放过程中发生错误（即图像文件损坏），QMovie将发出error()。

您可以通过调用setSpeed()来控制电影播放的速度，setSpeed()将原始速度的百分比作为参数。
通过调用setPaused（True）来暂停电影。 QMovie将进入暂停状态并发出stateChanged()。
如果您调用setPaused（False），QMovie将重新进入运行状态并再次启动电影。要停止电影，请使用stop()。

某些动画格式允许您设置背景颜色。你可以调用setBackgroundColor()来设置颜色，或者调用backgroundColor()来获取当前的背景颜色。

currentFrameNumber()返回当前帧的序列号。如果图像格式支持，frameCount()将返回动画中的总帧数。
您可以调用loopCount()来获取电影在完成前应循环的次数。 nextFrameDelay()返回当前帧应显示的毫秒数。

可以通过调用setCacheMode()来指示QMovie缓存动画帧。
调用supportedFormats()以获取QMovie支持的格式列表。
"""