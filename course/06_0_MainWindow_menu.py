#coding=utf-8

"""
1. 状态栏
2. 添加菜单和快捷键
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon
import sys


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.statusBar().showMessage('准备就绪') # showMessage()在状态栏上显示一条消息。

        self.setGeometry(300,300,400,300)
        self.setWindowTitle('--简单的菜单')

        # QAction是使用菜单栏，工具栏或自定义键盘快捷方式执行操作的抽象
        # 我们创建一个具有特定图标和“退出”标签的动作
        exitAct = QAction(QIcon('exit.png'), '退出(&E)', self)
        exitAct.setShortcut('Ctrl+Q')  # 为此操作定义了快捷方式
        exitAct.setStatusTip('退出程序') # 当我们将鼠标指针悬停在菜单项上时，第三行创建状态栏显示在状态栏中。
        exitAct.triggered.connect(qApp.quit) # 当我们选择这个特定的动作时，发出触发信号。 信号连接到QApplication小部件的quit()方法。

        # menuBar（）方法创建一个菜单栏。 我们使用addMenu（）创建文件菜单，并使用addAction（）添加操作。
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件(&F)')
        fileMenu.addAction(exitAct)
        """
        上面的代码中我们在退出、文件后面都增加了“&”这个符号，增加这个符号后，
        当我们按住“Alt+F”的时候就能快速打开文件这个菜单，同理按住“Alt+E”的时候就能退出了。
        """

        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())