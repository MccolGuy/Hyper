from PyQt4.QtGui import *
from PyQt4.QtGui import *
import subprocess
import ctypes, sys
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
is_admin()
def winpassword():
    user = input("사용자 이름")
    pw = input("새비밀번호")
    pw_list = list(pw)
    pw_num = len(pw)
    pw_ck = input("비밀번호 확인")
    def mkpw():
        if pw_num < 8:
            print("비밀번호는 8자리 이상 이여야합니다")
        elif pw_ck == pw:
            subprocess.call("net users %s %s" % (user, pw), shell=True)
        else:
            print("비밀번호가 일치하지 않습니다.")
if  is_admin():
    winpassword()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

app = QApplication(sys.argv)
xwin = XWindow()
app.exec_()