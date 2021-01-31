# coding:utf-8

""" 文本输入栏 QLineEdit

* 长度可以限制为 maxLength()
* 文本可以使用validator()或inputMask()或两者来任意约束。
* 更改行编辑的 echoMode()，还可以将其用作“只写”字段，以输入密码等输入。

* setText() 或 insert() 更改文本
* 可以使用setSelection()或selectAll()选择文本，并且可以使用cut()、copy() 和paste()。文本可以与setAlignment()对齐。

信号：
* 当文本改变发射textChanged()信号时；
* 当文本改变而不是通过调用setText()时，发出textEdited()信号
* 当光标移动时，cursorPositionChanged()信号被发射；
* 当按下Return或Enter键时，会发出returnPressed()信号。
* 编辑完成后，无论是因为行编辑失去焦点还是按下了Return / Enter键，editingFinished()都会发出。

样式：
* QLineEdits具有由平台样式指南指定的框架；你可以通过调用setFrame(Flase)来关闭它。
"""


""" 信号
selectionChanged() ：只要选择改变这个信号就会被发射。
cursorPositionChanged(int old, int new) ：只要光标移动，这个信号就会发射。前面的位置old，新的位置是new。
editingFinished()：按下返回或回车键或线条编辑失去焦点时发出此信号。
returnPressed()：按下返回或回车键时发出此信号。
textChanged(str)：只要文字发生变化就会发出此信号。文本参数是新文本。与textEdited()不同，当通过调用setText()以编程方式更改文本时，也会发出此信号。
textEdited(str) ：无论何时编辑文本都会发出此信号。文本参数是新文本。与textChanged()不同，当以编程方式更改文本时，不会发出此信号，例如通过调用setText()。

"""

"""
QLineEdit.setCompleter() ：输入栏的自动补全就是靠这个实现的，下下章我们讲解。
QLineEdit.deselect() ：取消选中任何已选中的文本。
QLineEdit.displayText()：返回显示的文本。默认值为一个空字符串。
如果echoMode是Normal，和text()返回的一样；如果EchoMode是Password或PasswordEchoOnEdit，会返回平台相关的密码掩码字符；如果EchoMode是NoEcho，返回一个空字符串””。
QLineEdit.selectedText()：返回选中的的文本。如果没有选中，返回一个空字符串。默认为一个空字符串。
QLineEdit.setCursorPosition(QLineEdit.cursorPosition)：设置输入框当前光标的位置。
QLineEdit.setMaxLength(int)：此属性包含文本的最大允许长度。如果文本太长，将从限制的位置截断。默认值为32767。
QLineEdit.setReadOnly(bool)：此属性保存输入框是否为只读。在只读模式下，用户仍然可以将文本复制到剪贴板，但不能编辑它，且不显示光标。
QLineEdit.setSelection(int start, int length) ：从位置start选择文本为length个字符，允许负长度。
"""