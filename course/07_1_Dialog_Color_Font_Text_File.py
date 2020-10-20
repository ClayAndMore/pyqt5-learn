#conding=utf-8

"""
ColorDialog, QFontDialog, QTextEdit, QFileDialog
QColorDialog, QFontDialog, QFileDialog分别负责颜色选择对话框、字体选择对话框、打开文件对话框
QTextEdit则是将刚才提到的类的结果用于呈现。QTextEdit能够呈现富文本。
"""

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QColorDialog, QFontDialog, QTextEdit, QFileDialog
import sys
class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    def initUI(self):

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('记得好看点')

        self.tx = QTextEdit(self)
        self.tx.setGeometry(20, 20, 300, 270)

        self.bt1 = QPushButton('打开文件',self)
        self.bt1.move(350,20)
        self.bt2 = QPushButton('选择字体',self)
        self.bt2.move(350,70)
        self.bt3 = QPushButton('选择颜色',self)
        self.bt3.move(350,120)

        self.bt1.clicked.connect(self.openfile)
        self.bt2.clicked.connect(self.choicefont)
        self.bt3.clicked.connect(self.choicecolor)

        self.show()

    def openfile(self):
        # getOpenFileName（）方法中的第一个字符串是标题。第二个字符串指定对话框工作目录
        fname = QFileDialog.getOpenFileName(self, '打开文件','./')
        # 如果增加文件过滤，可以改成如下语句：
        # fname = QFileDialog.getOpenFileName(self, '打开文件', './', ("Images (*.png *.xpm *.jpg)"))
        if fname[0]:
            with open(fname[0], 'r',encoding='gb18030',errors='ignore') as f:
                self.tx.setText(f.read())

    def choicefont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.tx.setCurrentFont(font)
            
    def choicecolor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.tx.setTextColor(col)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())