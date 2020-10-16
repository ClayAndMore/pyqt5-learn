# coding:utf-8
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow
from qttest import Ui_Form

if __name__ == "__main__":
    app = QApplication(sys.argv) # 每个pyqt程序必须创建一个application对象
    window = QMainWindow()

    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_()) # 程序主循环退出