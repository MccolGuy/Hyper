import subprocess
import time
import ctypes, sys
import getpass
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

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def mkpw():
    pw = input("새비밀번호\n")
    pw_list = list(pw)
    pw_num = len(pw)
    pw_ck = input("비밀번호 확인\n")
    if pw_num < 8:
        print("비밀번호는 8자리 이상 이여야합니다")
    elif pw_ck == pw:
        subprocess.call("net users %s %s" % (user, pw), shell=True)
    else:
        print("비밀번호가 일치하지 않습니다.")

if is_admin():
    mkpw()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
