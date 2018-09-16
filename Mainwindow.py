# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(525, 536)
        MainWindow.setMinimumSize(QtCore.QSize(525, 525))
        MainWindow.setMaximumSize(QtCore.QSize(550, 591))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KoPub돋움체 Medium"))
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(550, 550))
        self.centralwidget.setMaximumSize(QtCore.QSize(525, 525))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -10, 525, 525))
        self.frame.setMaximumSize(QtCore.QSize(525, 525))
        self.frame.setStyleSheet(_fromUtf8("QFrame{background-color:white}"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(160, 20, 201, 71))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_1 = QtGui.QPushButton(self.frame)
        self.pushButton_1.setGeometry(QtCore.QRect(70, 190, 171, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KoPub돋움체 Bold"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet(_fromUtf8("QPushButton{background-color:rgb(255, 170, 255)}\n"
"QPushButton{border-color:rgb(255, 170, 255)}"))
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 190, 171, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KoPub돋움체 Bold"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8("QPushButton{background-color:rgb(255, 255, 127)}\n"
"QPushButton{font-color:rgb(255, 170, 255)}"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(370, 490, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KoPub바탕체 Medium"))
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 525, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("나눔바른고딕 UltraLight"))
        self.menu.setFont(font)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/icon/Hyper_logo.png\"/></p></body></html>", None))
        self.pushButton_1.setText(_translate("MainWindow", "점검시작", None))
        self.pushButton_2.setText(_translate("MainWindow", "편의 기능", None))
        self.label_2.setText(_translate("MainWindow", "made by Hyper Team", None))
        self.menu.setTitle(_translate("MainWindow", "점검설정", None))

import logoicon_rc
