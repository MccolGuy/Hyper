import os
import subprocess
from win32com.client import Dispatch
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
print(Hncupdate)

def hncupdate():
    os.chdir("C:\\Program Files (x86)\\Hnc\\HncUtils\\Update")
    subprocess.call("HncUpdate90.exe", shell=True)