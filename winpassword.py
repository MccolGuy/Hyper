import subprocess
import ctypes, sys
user = input( "사용자 이름\n")
pw = input("새비밀번호\n")
pw_list =  list(pw)
pw_num = len(pw)
pw_ck =input("비밀번호 확인\n")
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def mkpw():
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
