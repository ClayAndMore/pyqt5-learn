from PyQt5.QtWidgets import QLineEdit, QApplication, QDialog, QAction, QMessageBox
from PyQt5.QtGui import QIcon
import sys
from checkword import correct

class Line(QDialog):
    def __init__(self):
        super().__init__()
        self.Ui()
    
    def Ui(self):
        self.resize(450,100)
        self.setWindowTitle('单词拼写检查')
        self.line = QLineEdit(self)
        self.line.move(20,20)
        # 创建一个action 放置图标按钮, 当点击时触发 check
        action = QAction(self)
        action.setIcon(QIcon('check.ico'))
        action.triggered.connect(self.Check)

        """ QLineEdit.AcionPosition
        描述如何显示加入到输入框中到 action 部件。
        * OLineEdit.LeadingPosition  当使用布局方向Qt.LeftToRight 时, 部件显示在文本左侧；使用Qt.RightToLeft时，则显示在右侧。
        * QLineEdit.TrailingPosition  当使用布局方向Qt.LeftToRight 时，部件显示在文本右侧； 使用Qt.RightToLeft时，则显示在左侧。
        """

        self.line.addAction(action,QLineEdit.TrailingPosition)
        self.show()
    
    def Check(self):
        word = self.line.text()
        # correct 拼写检查器：https://blog.csdn.net/sky_money/article/details/7957996
        if correct(word) != word:
            QMessageBox.information(self,'提示信息','你或许想要表达的单词是：'+correct(word))
        else:
            QMessageBox.information(self,'提示信息','你填写的单词是：'+word)

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    line = Line()
    sys.exit(app.exec_())


