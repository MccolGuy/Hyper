from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
import Mainwindow, checkmn
import sys
class Second(QDialog, checkmn.Ui_Dialog):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)
        self.setupUi(self)
        global a
        a = self.checkBox_1.isChecked()
        while a == 1:
            print(a)


class First(QMainWindow, Mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_1.clicked.connect(self.open_checkmn)
        self.dialog = Second(self)
        # 메인윈도우 보이기
        self.show()

    def open_checkmn(self):
        self.dialog.show()
def main():
    app = QtGui.QApplication(sys.argv)
    main = First()
    main.show()
    sys.exit(app.exec_())
    print(a)
if __name__ == '__main__':
    main()
