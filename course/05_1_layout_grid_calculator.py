# coding: utf-8
"""
栅格布局将位于其中的窗口部件放入一个网状的栅格之中。
QGridLayout需要将提供给它的空间划分成的行和列，并把每个窗口部件插入并管理到正确的单元格。

栅格布局是这样工作的：它计算了位于其中的空间，
然后将它们合理的划分成若干个行（row）和列（column），并把每个由它管理的窗口部件放置在合适的单元之中，
这里所指的单元（cell）即是指由行和列交叉所划分出来的空间。
"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QGridLayout, QLCDNumber)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()

    def Init_UI(self):
        # 创建QGridLayout的实例并将其设置为应用程序窗口的布局。
        grid = QGridLayout()
        self.setLayout(grid)

        self.setGeometry(300,300,400,300)
        self.setWindowTitle('计算器')

        # 如果我们向窗格添加窗口小部件，我们可以提供窗口小部件的行跨度和列跨度。
        self.lcd = QLCDNumber()
        grid.addWidget(self.lcd,0,0,3,0)
        grid.setSpacing(10)

        names = ['Cls', 'Bc', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i,j) for i in range(4,9) for j in range(4,8)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
            button.clicked.connect(self.Cli)

        self.show()

    def Cli(self):
        sender = self.sender().text()
        ls = ['/', '*', '-', '=', '+']
        if sender in ls:
            self.lcd.display('A')
        else:
            self.lcd.display(sender)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())