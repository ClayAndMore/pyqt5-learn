# coding:utf-8

# QLCDNumber小部件显示一个类似LCD的数字。
import sys
from PyQt5.QtWidgets import QWidget, QLCDNumber, QLabel, QApplication
from PyQt5.QtCore import QTimer, QDateTime, QDate, QTime

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.resize(370,190)
        self.setWindowTitle('倒计时：LCD数字')

        lb = QLabel("距离2022年北京-张家口冬季奥林匹克运动会还有", self)
        lb.move(80, 60)

        self.lcd = QLCDNumber(self)
        self.lcd.move(80, 100)

        self.lcd.setDigitCount(12) # 将新建的QLCDNumber对象设置为12位。
        self.lcd.setMode(QLCDNumber.Dec) # setMode()该属性保存当前的显示模式（数字库）
        self.lcd.setSegmentStyle(QLCDNumber.Flat)#Mac系统需要加上，否则下面的color不生效。
        # setStyleSheet()设置LCD的外观， 有点像css
        self.lcd.setStyleSheet("border: 2px solid black; color: red; background: silver;")

        time = QTimer(self)
        time.setInterval(1000) # 超时间隔是1000ms（1秒），所以每隔1秒我们就会调用refresh()这个槽函数
        time.timeout.connect(self.refresh)
        time.start()

        self.show()

    def refresh(self):
        # 使用了currentMSecsSinceEpoch()将其转换成当前时间到1970-01-01T00：00：00世界协调时间以来的毫秒数。
        startDate = QDateTime.currentMSecsSinceEpoch()
        endDate = QDateTime(QDate(2022, 2, 4), QTime(0, 0, 0)).toMSecsSinceEpoch()
        interval = endDate - startDate
        print(interval)
        if interval > 0:
            days = interval // (24 * 60 * 60 * 1000)
            hour = (interval - days * 24 * 60 * 60 * 1000) // (60 * 60 * 1000)
            min = (interval - days * 24 * 60 * 60 * 1000 - hour * 60 * 60 * 1000) // (60 * 1000)
            sec = (interval - days * 24 * 60 * 60 * 1000 - hour * 60 * 60 * 1000 - min * 60 * 1000) // 1000
            intervals = str(days) + ':' + str(hour) + ':' + str(min) + ':' + str(sec)
            self.lcd.display(intervals)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())