# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkmn.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(525, 525)
        Dialog.setMinimumSize(QtCore.QSize(525, 525))
        Dialog.setMaximumSize(QtCore.QSize(525, 525))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 525, 525))
        self.frame.setMinimumSize(QtCore.QSize(525, 525))
        self.frame.setMaximumSize(QtCore.QSize(525, 525))
        self.frame.setStyleSheet(_fromUtf8("QFrame{background-color:white}"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.checkBox_1 = QtGui.QCheckBox(self.frame)
        self.checkBox_1.setGeometry(QtCore.QRect(20, 60, 221, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KoPub돋움체 Light"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_1.setFont(font)
        self.checkBox_1.setObjectName(_fromUtf8("checkBox_1"))
        self.checkBox_2 = QtGui.QCheckBox(self.frame)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 90, 221, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KoPub돋움체 Light"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.frame)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 120, 321, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KoPub돋움체 Light"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_4 = QtGui.QCheckBox(self.frame)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 150, 221, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KoPub돋움체 Light"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox_5 = QtGui.QCheckBox(self.frame)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 180, 291, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KoPub돋움체 Light"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_6 = QtGui.QCheckBox(self.frame)
        self.checkBox_6.setGeometry(QtCore.QRect(20, 210, 221, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KoPub돋움체 Light"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.checkBox_7 = QtGui.QCheckBox(self.frame)
        self.checkBox_7.setGeometry(QtCore.QRect(20, 240, 221, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KoPub돋움체 Light"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setCheckable(True)
        self.checkBox_7.setAutoRepeat(False)
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.checkBox_8 = QtGui.QCheckBox(self.frame)
        self.checkBox_8.setGeometry(QtCore.QRect(20, 270, 221, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KoPub돋움체 Light"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KoPub돋움체 Bold"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.buttonBox = QtGui.QDialogButtonBox(self.frame)
        self.buttonBox.setGeometry(QtCore.QRect(170, 480, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.checkBox_1.setText(_translate("Dialog", "윈도우 업데이트", None))
        self.checkBox_2.setText(_translate("Dialog", "바이러스 백신 점검", None))
        self.checkBox_3.setText(_translate("Dialog", "한글프로그램의 최신 보안 패치 설치 여부 점검", None))
        self.checkBox_4.setText(_translate("Dialog", "로그인 패스워드 점검", None))
        self.checkBox_5.setText(_translate("Dialog", "미사용 ActiveX 프로그램 존재 여부 점검", None))
        self.checkBox_6.setText(_translate("Dialog", "화면보호기 설정 여부 점검", None))
        self.checkBox_7.setText(_translate("Dialog", "사용자 공유폴더 설정 여부 점검", None))
        self.checkBox_8.setText(_translate("Dialog", "USB 자동 실행 허용 여부 점검", None))
        self.label.setText(_translate("Dialog", "점검항목", None))

