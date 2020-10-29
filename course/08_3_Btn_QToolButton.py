# coding:utf-8

"""
工具按钮
连接跳转
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QToolButton, QAction
from PyQt5.QtCore import QTimer, Qt, QUrl
from PyQt5.QtGui import QIcon, QDesktopServices

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 100)
        """
        Qt.ToolButtonTextBesideIcon: 该属性保持工具按钮是仅显示图标，仅显示文本，还是显示图标旁边/下方的文本。
        - Qt.ToolButtonIconOnly 只显示图标
        - Qt.ToolButtonTextOnly 只显示文字
        - Qt.ToolButtonTextBesideIcon 文字出现在图标旁
        - Qt.ToolButtonTextUnderIcon 文字出现在图标下方
        - Qt.ToolButtonFollowStyle 按钮的样式遵循系统设置， 在Unix上，将使用来自桌面环境的用户设置。 在其他平台上，Qt.ToolButtonFollowStyle只意味着图标。
        
        
        """

        tb = QToolButton(self)
        tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # tb.setArrowType(Qt.DownArrow)  # 设置按钮是否显示一个箭头，而不是一个正常的图标。
        tb.setToolTip('选择适合你的支付方式')

        """ setPopupMode 描述弹出式菜单与工具按钮一起使用的方式:
        DelayedPopup: 按下按钮一定时间后，才显示菜单。
        MenuButtonPopup: 工具按钮旁边会显示一个特殊的箭头，按下箭头部分显示菜单。
        InstantPopup: 按下工具按钮时菜单显示，没有延迟，这种模式下按钮本身的动作不会被触发。
        """

        tb.setPopupMode(QToolButton.MenuButtonPopup)
        tb.setText('支付方式')
        tb.setIcon(QIcon('icon/bank.ico'))
        tb.setAutoRaise(True) # 否启用自动升起

        menu = QMenu(self)
        self.alipayAct = QAction(QIcon('icon/alipay.ico'), '支付宝支付', self)
        self.wechatAct = QAction(QIcon('icon/wechat.ico'), '微信支付', self)
        self.visaAct = QAction(QIcon('icon/visa.ico'), 'Visa卡支付', self)
        self.master_cardAct = QAction(QIcon('icon/master_card.ico'), '万事达卡支付', self)

        menu.addAction(self.alipayAct)
        menu.addAction(self.wechatAct)
        menu.addSeparator() # 之前说过，收设置分割线。
        menu.addAction(self.visaAct)
        menu.addAction(self.master_cardAct)

        tb.setMenu(menu)
        self.show()

        self.alipayAct.triggered.connect(self.on_click)
        self.wechatAct.triggered.connect(self.on_click)
        self.visaAct.triggered.connect(self.on_click)
        self.master_cardAct.triggered.connect(self.on_click)

    def on_click(self):
        # 调用系统默认的浏览器去打开指定的网页。QUrl类为使用URL提供了一个方便的接口。
        if self.sender() == self.alipayAct:
            QDesktopServices.openUrl(QUrl('https://www.alipay.com/'))
        elif self.sender() == self.wechatAct:
            QDesktopServices.openUrl(QUrl('https://pay.weixin.qq.com/index.php'))
        elif self.sender() == self.visaAct:
            QDesktopServices.openUrl(QUrl('https://www.visa.com.cn/'))
        else:
            QDesktopServices.openUrl(QUrl('https://www.mastercard.com.cn/zh-cn.html'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())