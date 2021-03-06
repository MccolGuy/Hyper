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
import tkinter as tk
import glob
from tkinter import filedialog
import shutil
winpassword = 2
scnprotecter = 2
stopusbauto = 2
Hncupdate = 2
alyacupdate = 2
checklist = [winpassword,scnprotecter,stopusbauto,Hncupdate,alyacupdate]
class Third(QDialog, checkst.Ui_Dialog):
    def __init__(self, parent=None):
        super(Third, self).__init__(parent)
        HncUpdateCheck()
        stopusbautocheck()
        scnprotectercheck()
        winpasswordcheck()
        self.setupUi(self)
        self.autostart.clicked.connect(self.start_start)
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
            self.st_5.setText("안전")
        if Hncupdate == 1:
            self.st_2.setText("취약") 
        else:
            self.st_2.setText("안전")
    def start_start(self):
        if winpassword == 1:
            print("윈도우 패스워드 재설정")
            if is_admin():
                mkpw()
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        if scnprotecter == 1:
                    print("화면보호기 설정")
                    scnprotecterset()
        if stopusbauto == 1:
                    print("USB 자동실행 방지 설정")
                    stopusbautoset()
        if Hncupdate == 1:
                    print("한컴오피스 업데이트")
                    hncupdate()

class Second(QDialog, checkmn.Ui_Dialog):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)
        self.setupUi(self)
        self.dialog02 = Third()
        self.pushButton.clicked.connect(self.checkstart)
        stopusbautocheck()
        winpasswordcheck()
        HncUpdateCheck()

    def checkstart(self):

        self.dialog02.show()

class First(QMainWindow, Mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_1.clicked.connect(self.open_checkmn)
        self.pushButton_2.clicked.connect(self.startfileorg)
        self.dialog = Second(self)
        # 메인윈도우 보이기
        self.show()

    def open_checkmn(self):

        self.dialog.show()
    def startfileorg(self):
        fileorganizer()
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
        stopusbauto = 0
    else:
        stopusbauto = 1
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
    hncnewversion = lines[0]
    ver_parser = Dispatch('Scripting.FileSystemObject')
    path = "C:\\Program Files\\Hnc\\HOffice9\\Bin\\Hwp.exe"
    info = ver_parser.GetFileVersion(path)
    a1 = hncnewversion[0]
    b1 = info[0]
    a2 = hncnewversion[2]
    b2 = info[2]
    a3 = hncnewversion[4]
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
    os.chdir("C:\\Program Files\\Hnc\\HncUtils\\Update")
    subprocess.call("HncUpdate90.exe", shell=True)
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
    sccheck = get_reg_scnprotecter("ScreenSaveActive")
    if sccheck == 1:
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
    set_reg_scnprotecter("ScreenSaveActive", 1)
def winpasswordcheck():
    global winpassword
    user = getpass.getuser()
    updatedate = ("net user %s | findstr 마지막 "%(user))
    u_value = subprocess.check_output((updatedate),shell=True)
    a = str(u_value)
    b = a[114:116]
    c = time.strftime('%m', time.localtime(time.time()))
    d = int(b) - int(c)
    if d >= 2:
        winpassword = 1
    else:
        winpassword = 0
def fileorganizer():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()
    os.chdir(file_path)
    print(file_path)
    jpg_list = glob.glob(file_path + "/*.jpg")
    exe_list = glob.glob(file_path + "/*.exe")
    png_list = glob.glob(file_path + "/*.png")
    pptx_list = glob.glob(file_path + "/*.pptx")
    zip_list = glob.glob(file_path + "/*.zip")
    hwp_list = glob.glob(file_path + "/*.hwp")
    if os.path.isdir(file_path + "/jpg"):
        for i in jpg_list:
            shutil.move(i, file_path + "/jpg")
    else:
        os.mkdir(file_path + "/jpg")
        for i in jpg_list:
            shutil.move(i, file_path + "/jpg")
    print("jpg 파일 분류중")
    if os.path.isdir(file_path + "/exe"):
        for i in exe_list:
            shutil.move(i, file_path + "/exe")
    else:
        os.mkdir(file_path + "/exe")
        for i in exe_list:
            shutil.move(i, file_path + "/exe")
    print("exe 파일 정리중")
    if os.path.isdir(file_path + "/png"):
        for i in png_list:
            shutil.move(i, file_path + "/png")
    else:
        os.mkdir(file_path + "/png")
        for i in png_list:
            shutil.move(i, file_path + "/png")
    print("png 파일 정리중")
    if os.path.isdir(file_path + "/pptx"):
        for i in pptx_list:
            shutil.move(i, file_path + "/pptx")
    else:
        os.mkdir(file_path + "/pptx")
        for i in pptx_list:
            shutil.move(i, file_path + "/pptx")
    print("pptx 파일 정리중")
    if  os.path.isdir(file_path + "/zip"):
        for i in zip_list:
            shutil.move(i, file_path + "/zip")
    else:
        os.mkdir(file_path + "/zip")
        for i in zip_list:
            shutil.move(i, file_path + "/zip")
    print("zip 파일 정리중")
    if os.path.isdir(file_path + "/hwp"):
        for i in hwp_list:
            shutil.move(i, file_path + "/hwp")
    else:
        os.mkdir(file_path + "/hwp")
        for i in hwp_list:
            shutil.move(i, file_path + "/hwp")
    print("hwp 파일 정리중")
    print("파일 분류가 완료 되었습니다.")
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

def main():
    app = QtGui.QApplication(sys.argv)
    main = First()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()