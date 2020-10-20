# coding=utf-8

# 进度条对话框

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QProgressDialog)
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 150)
        self.setWindowTitle("进度对话框")

        self.lb = QLabel("文件数量", self)
        self.lb.move(20, 40)

        self.bt1 = QPushButton('开始', self)
        self.bt1.move(20, 80)

        self.edit = QLineEdit('100000', self)
        self.edit.move(100, 40)

        self.show()

        self.bt1.clicked.connect(self.showDialog)

    def showDialog(self):
        num = int(self.edit.text())
        progress = QProgressDialog(self)
        progress.setWindowTitle("请稍等")
        progress.setLabelText("正在操作...")
        progress.setCancelButtonText("取消")
        # 它估计操作所花费的时间（基于步骤的时间），并且只有当该估计值超出minimumDuration() （默认为4秒）时才显示。
        progress.setMinimumDuration(5)
        # 此属性保留由模态小部件阻止的窗口。
        progress.setWindowModality(Qt.WindowModal)

        # 使用setMinimum() 和setMaximum() 或构造函数来设置操作中的“steps”数量，并在操作进行时调用setValue()。
        # setRange(0,num)就是设置其最小和最大值
        progress.setRange(0, num)
        for i in range(num):
            progress.setValue(i)
            if progress.wasCanceled():
                QMessageBox.warning(self, "提示", "操作失败")
                break
        else:
            progress.setValue(num)
            QMessageBox.information(self, "提示", "操作成功")


"""
补充：
如果任务的预期持续时间小于minimumDuration，则对话框根本不会出现。这样可以防止弹出对话框，快速完成任务。
对于预期超过minimumDuration的任务，对话框将在minimumDuration时间之后或任何进度设置后立即弹出。
如果设置为0，则只要设置任何进度，将始终显示对话框。 默认值为4000毫秒,即4秒。

progress.setWindowModality(Qt.WindowModal)
这个属性只对Windows有意义。 模态小部件防止其他窗口中的小部件获取输入。 该属性的值控制在窗口小部件可见时阻止哪些窗口。 
窗口可见时更改此属性无效; 您必须首先hide（）小部件，然后再次show（）。
"""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())