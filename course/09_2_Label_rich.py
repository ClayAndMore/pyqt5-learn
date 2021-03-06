# coding=utf-8

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(400, 300)
        self.setWindowTitle('标签:富文本（QLabel）')

        lb = QLabel(self)
        lb.resize(400, 200)

        html = '''
                <style type="text/css">
                    table.imagetable {
                        font-family: verdana,arial,sans-serif;
                        font-size:11px;
                        color:#333333;
                        border-width: 1px;
                        border-color: #999999;
                        border-collapse: collapse;
                    }
                    table.imagetable th {
                        background:#b5cfd2 url('cell-blue.jpg');
                        border-width: 1px;
                        padding: 8px;
                        border-style: solid;
                        border-color: #999999;
                    }
                    table.imagetable td {
                        background:#dcddc0 url('cell-grey.jpg');
                        border-width: 1px;
                        padding: 8px;
                        border-style: solid;
                        border-color: #999999;
                    }
                </style>

                <table class="imagetable">
                    <tr>
                        <th>Info Header 1</th><th>Info Header 2</th><th>Info Header 3</th>
                    </tr>
                    <tr>
                        <td>Text 1A</td><td>Text 1B</td><td>Text 1C</td>
                    </tr>
                    <tr>
                        <td>Text 2A</td><td>Text 2B</td><td>Text 2C</td>
                    </tr>
                </table>
            '''
        lb.setText(html)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())