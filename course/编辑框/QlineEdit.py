from PyQt5.QtWidgets import QLineEdit, QApplication, QDialog, QLabel, QMessageBox
import sys

class Line(QDialog):
    def __init__(self):
        super().__init__()
        self.Ui()
    
    def Ui(self):
        self.resize(300,100)
        # self.setWindowTitle('出现就选择文本')
        self.setWindowTitle('信号发射')
        self.line = QLineEdit(self)
        line2 = QLineEdit(self)
        line3 = QLineEdit(self)
        line4 = QLineEdit(self)

        lb = QLabel('IP地址',self)
        lb2 = QLabel('MAC地址',self)
        lb3 = QLabel('日期',self)
        lb4 = QLabel('License',self)
        
        lb.move(10,10)
        lb2.move(10,30)
        lb3.move(10,50)
        lb4.move(10,70)

        self.line.move(60,10)
        line2.move(60,30)
        line3.move(60,50)
        line4.move(60,70)

        # 按下返回或回车键或线条编辑失去焦点时发出此信号。
        self.line.editingFinished.connect(self.Action)

        self.line.setInputMask('000.000.000.000;_') # 设置掩码
        # line2.setInputMask('HH:HH:HH:HH:HH:HH;_')
        # line3.setInputMask('0000-00-00')
        # line4.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')

        # line.setText('请在这里输入姓名！')
        # line.setSelection(0,len(line.text()))
        self.show()

    def Action(self):
        if len(self.line.text()) > 3:
            QMessageBox.information(self,'提示信息', '这行你完成了哦')

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    line = Line()
    sys.exit(app.exec_())


