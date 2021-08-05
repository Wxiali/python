# content of test_APK_com.py
# coding=gbk
import base64
import multiprocessing
import os
import re
import getpass
import sys
import time

user_name = getpass.getuser()  # ��ȡ��ǰ�û���
# δ�޸ĵ��ı�·��
oldpath = 'C:/Users/' + user_name + '/Desktop/ruiyin.txt'
# �޸ĺ���ı�·��
newpath = 'C:/Users/' + user_name + '/Desktop/ruiyin.cfg'
# ����һ��AaptLog.txt�ı�
aaptLog = 'C:\\Users\\' + user_name + '\\Desktop\\AaptLog.txt'

class packagename_activity:
    def get_packagename(self, path):
        aapt = []
        os.system(f'aapt dump badging C:\\Users\\{user_name}\\Desktop\\apk\\{path}> C:\\Users\\{user_name}\\Desktop'
                  f'\\AaptLog.txt')
        with open('C:\\Users\\' + user_name + '\\Desktop\\AaptLog.txt', 'rb') as f:
            p1 = "package: name='(.+?)'"
            results1 = re.finditer(pattern=p1, string=f.readline().decode('utf-8'))
            for r in results1:
                packagename = r.group(1)
                aapt.append(packagename)
        return aapt


# ����txt�ļ�
def create_text(filename):
    path = 'C:/Users/' + user_name + '/Desktop/'
    file_path = path + filename + '.txt'
    file = open(file_path, 'w')
    file.close()


# ����AaptLog.txt�ļ�
def create_aaptLog():
    file = open(aaptLog, 'w')
    file.close()


def oldFile(oldpath):
    # �����ruiyin.txt�ı�
    with open(oldpath, "r+") as f:
        f.seek(0)
        f.truncate()


def newFile(newpath):
    # ���ruiyin.cfg�ı�
    with open(newpath, "r+") as f:
        f.seek(0)
        f.truncate()


# ������ruiyin.cfg
def writeTxtFlie(oldepath):
    a = packagename_activity()
    # ��ȡ·��
    lujing = "C:\\Users\\" + user_name + "\\Desktop\\apk"
    # �õ�·���µ�apk
    li = os.listdir(lujing)
    # ����ruiyin.txt
    create_text('ruiyin')
    # �����ruiyin.txt
    oldFile(oldpath)
    # ѭ�����������base64������base64����д��ruiyin.txt
    for j in li:
        # ��ȡapk����
        packageName = a.get_packagename(j)
        nameObj = ''.join(packageName)
        # ��ȡ����base64
        basepackageName = base64.b64encode(nameObj.encode('utf-8'))
        # ��base64����
        flashback = str(basepackageName, 'utf-8')[::-1]
        # д��ruiyin.txt
        with open(oldepath, 'a', encoding='utf-8') as file1:
            file1.write(flashback + '\n')
            file1.close()
        continue


# ����ruiyin.cfg
def writeCfgFlie(newpath):
    a = packagename_activity()
    # ��ȡ·��
    lujing = "C:\\Users\\" + user_name + "\\Desktop\\apk"
    # �õ�·���µ�apk
    li = os.listdir(lujing)
    # �����ruiyin.cfg
    newFile(newpath)
    # ѭ�����������base64������base64����д��ruiyin.cfg
    for j in li:
        # ��ȡapk����
        packageName = a.get_packagename(j)
        nameObj = ''.join(packageName)
        # ��ȡ����base64
        basepackageName = base64.b64encode(nameObj.encode('utf-8'))
        # ��base64����
        flashback = str(basepackageName, 'utf-8')[::-1]
        # д��ruiyin.cfg
        with open(newpath, 'a', encoding='utf-8') as file:
            file.write(flashback + '\n')
            file.close()
        continue


if __name__ == '__main__':
    create_aaptLog()
    # �ж��Ƿ����ruiyin.cfg
    if os.access(newpath, os.F_OK):
        # ���ڵ���
        writeCfgFlie(newpath)
    else:
        # �����ڵ���
        writeTxtFlie(oldpath)
        # �޸�ruiyin.txtΪruiyin.cfg
        os.rename(oldpath, newpath)
    os.remove(aaptLog)
    print('ִ�гɹ���������ruiyin.cfg�ļ�')
    time.sleep(2)
