from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
import Mainwindow, checkmn, checkst
import subprocess
import getpass
import ctypes
import winreg
import os
import sys
import time
from win32com.client import Dispatch
winpassword = 2
scnprotecter = 2
stopusbauto = 2
Hncupdate = 2
alyacupdate = 2
checklist = [winpassword,scnprotecter,stopusbauto,Hncupdate,alyacupdate]
class Third(QDialog, checkst.Ui_Dialog):
    def __init__(self, parent=None):
        super(Third, self).__init__(parent)
        self.setupUi(self)
        if winpassword == 1:
            self.st_3.setText("취약")
        else:
            self.st_3.setText("안전")
        if scnprotecter == 1:
            self.st_4.setText("취약")
        else:
            self.st_4.setText("안전")
        if stopusbauto == 1:
            self.st_5.setText("취약")
        else:
            self.st5.setText("안전")
        if Hncupdate == 1:
            self.st_2.setText("취약")
        else:
            self.st_2.setText("안전")
        if alyacupdate == 1:
            self.st1.setText("취약")
        else:
            self.st1.setText("안전")

class Second(QDialog, checkmn.Ui_Dialog):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.startcheck)
        self.dialog = Third(self)
    def startcheck(self):
        stopusbautocheck()
        HncUpdateCheck()
        alyacUpdateCheck()
        scnprotectercheck()
        winpasswordcheck()
        self.dialog.show()
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

def stopusbautocheck():
    global stopusbauto
    stopusbauto_reg = r"SYSTEM\CurrentControlSet\Services\cdrom"


    def get_reg_stopusbauto(name):
        try:
            registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, stopusbauto_reg, 0,
                                           winreg.KEY_READ)
            value, regtype = winreg.QueryValueEx(registry_key, name)
            winreg.CloseKey(registry_key)
            return value
        except WindowsError:
            return None
    autoruncheck = get_reg_stopusbauto('AutoRun')
    if autoruncheck == 1:
        stopusbauto = 1
    else:
        stopusbauto = 0
def stopusbautoset():
    stopusbauto_reg = r"SYSTEM\CurrentControlSet\Services\cdrom"
    def set_reg_stopusbauto(name, value):
        try:
            winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, stopusbauto_reg)
            registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, stopusbauto_reg, 0,
                                           winreg.KEY_WRITE)
            winreg.SetValueEx(registry_key, name, 0, winreg.REG_DWORD, value)
            winreg.CloseKey(registry_key)
            return True
        except WindowsError:
            return False
    set_reg_stopusbauto("Autorun",0)
def HncUpdateCheck():
    global Hncupdate
    f = open('setting\\setting.txt')
    lines = f.readlines()
    Hncnewversion = lines[0]
    ver_parser = Dispatch('Scripting.FileSystemObject')
    path = "C:\\Program Files (x86)\\Hnc\\Hwp80\\Hwp.exe"
    info = ver_parser.GetFileVersion(path)
    print(info)
    a1 = Hncnewversion[0]
    b1 = info[0]
    a2 = Hncnewversion[2]
    b2 = info[2]
    a3 = Hncnewversion[4]
    b3 = info[4]
    if a1 > b1:
        Hncupdate = 1
    elif a1 == b1[0]:
        if a2 > b2:
            Hncupdate = 1
    elif a3 > b3:
        Hncupdate = 1
    else:
        Hncupdate = 0
def hncupdate():
    os.chdir("C:\\Program Files (x86)\\Hnc\\HncUtils\\Update")
    subprocess.call("HncUpdate90.exe", shell=True)
def alyacUpdateCheck():
    global alyacupdate
    alyacupdate_reg = r"SOFTWARE\ESTsoft\ALYac"
    c = time.strftime('20%y%m%d', time.localtime(time.time()))
    def set_reg_alyacupdate(name, value):
        try:
            winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, alyacupdate_reg)
            registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, alyacupdate_reg, 0,
                                           winreg.KEY_WRITE)
            winreg.SetValueEx(registry_key, name, 0, winreg.REG_DWORD, value)
            winreg.CloseKey(registry_key)
            return True
        except WindowsError:
            return False

    def get_reg_alyacupdate(name):
        try:
            registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, alyacupdate_reg, 0,
                                           winreg.KEY_READ)
            value, regtype = winreg.QueryValueEx(registry_key, name)
            winreg.CloseKey(registry_key)
            return value
        except WindowsError:
            return None
    a = get_reg_alyacupdate("dbUpdateDate")
    b = a[0:8]
    if c == a:
        alyacupdate = 0
    else:
        alyacupdate = 1
def alyacupdate():
    os.chdir("C:\Program Files\ESTsoft\ALYac")
    subprocess.call("AYUpdate.exe", shell=True)
def scnprotectercheck():
    global scnprotecter
    scnprotecter_reg = r"Control Panel\Desktop"

    def get_reg_scnprotecter(name):
        try:
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, scnprotecter_reg, 0,
                                           winreg.KEY_READ)
            value, regtype = winreg.QueryValueEx(registry_key, name)
            winreg.CloseKey(registry_key)
            return value
        except WindowsError:
            return None

    #Example MouseSensitivity
    #Read value
    sccheck = get_reg_scnprotecter('ScreenSaveActive')
    if sccheck == 0:
        scnprotecter = 1
    else:
        scnprotecter = 0
def scnprotecterset():
    scnprotecter_reg = r"Control Panel\Desktop"
    def set_reg_scnprotecter(name, value):
        try:
            winreg.CreateKey(winreg.HKEY_CURRENT_USER, scnprotecter_reg)
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, scnprotecter_reg, 0,
                                           winreg.KEY_WRITE)
            winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
            winreg.CloseKey(registry_key)
            return True
        except WindowsError:
            return False
    set_reg_scnprotecter("ScreenSaveActive",1)
def winpasswordcheck():
    user = getpass.getuser()
    updatedate = ("net user %s | findstr 마지막 "%(user))
    u_value = subprocess.check_output((updatedate),shell=True)
    a = str(u_value)
    b = a[114:116]
    c = time.strftime('%m', time.localtime(time.time()))
    d = int(b) - int(c)
    if d >= 2:
        winpassword = 0
    else:
        winpassword = 1

def mkpw():
    user = getpass.getuser()
    pw = input("새비밀번호\n")
    pw_num = len(pw)
    pw_ck = input("비밀번호 확인\n")
    if pw_num < 8:
        print("비밀번호는 8자리 이상 이여야합니다")
    elif pw_ck == pw:
        subprocess.call("net users %s %s" % (user, pw), shell=True)
    else:
        print("비밀번호가 일치하지 않습니다.")
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    mkpw()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)































def main():
    app = QtGui.QApplication(sys.argv)
    main = First()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
