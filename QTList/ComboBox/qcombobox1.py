from PyQt5.QtWidgets import QApplication, QComboBox, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon
import sys

class ExComboBox(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.resize(400,100)
        self.setWindowTitle("股票")
        self.show()

        label1 = QLabel("你可以选择", self)
        combox = QComboBox(self)
        label2 = QLabel("大家静一静，", self)
        self.label3 = QLabel("        ", self)

        hlayout1 = QHBoxLayout()
        hlayout1.addStretch(1)
        hlayout1.addWidget(label1)
        hlayout1.addStretch(1)
        hlayout1.addWidget(combox)
        hlayout1.addStretch(1)

        hlayout2 = QHBoxLayout()
        hlayout2.addStretch(1)
        hlayout2.addWidget(label2)
        hlayout2.addStretch(1)
        hlayout2.addWidget(self.label3)
        hlayout2.addStretch(1)

        vlayout = QVBoxLayout()
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)

        self.setLayout(vlayout)

        infomation = ["我想静静", "我要开始学习了", "我要开始睡觉了", "我要开始装B了"]

        combox.addItems(infomation)

        self.label3.setText(combox.currentText())

        combox.activated[str].connect(self.zhuangB)
    
    def zhuangB(self, text):
        self.label3.setText(text)
        if text == "我要开始装B了":
            msgBox = QMessageBox(QMessageBox.NoIcon, '装B',"让你装B")
            msgBox.setIconPixmap(QPixmap("./res/zhuangB.png"))
            msgBox.setWindowIcon(QIcon("./res/latin_b.png"))
            msgBox.exec()

app = QApplication(sys.argv)
ex = ExComboBox()
sys.exit(app.exec_())