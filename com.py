# coding=gbk
import base64
import os
import re

import getpass

user_name = getpass.getuser()  # ��ȡ��ǰ�û���
# δ�޸ĵ��ı�·��
packge = 'C:/Users/' + user_name + '/Desktop/com.txt'
oldpath = 'C:/Users/' + user_name + '/Desktop/ruiyin.txt'
# �޸ĺ���ı�·��
newpath = 'C:/Users/' + user_name + '/Desktop/ruiyin.cfg'


# ����txt�ļ�
def create_text(filename):
    path = 'C:/Users/' + user_name + '/Desktop/'
    file_path = path + filename + '.txt'
    file = open(file_path, 'w')
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


# ������ruiyin.cfg����
def writeTxtFlie(oldepath):
    # ����ruiyin.txt
    create_text('ruiyin')
    # �����ruiyin.txt
    oldFile(oldpath)
    # ѭ�����������base64������base64����д��ruiyin.txt
    with open(packge, "r") as f:
        for line in f.readlines():
            line = line.strip('\n')  # ȥ���б���ÿһ��Ԫ�صĻ��з�
            basepackageName = base64.b64encode(line.encode('utf-8'))
            # ��base64����
            flashback = str(basepackageName, 'utf-8')[::-1]
            # д��ruiyin.txt
            with open(oldepath, 'a', encoding='utf-8') as file1:
                file1.write(flashback + '\n')
                file1.close()


# ����ruiyin.cfg����
def writeCfgFlie(newpath):
    # �����ruiyin.cfg
    newFile(newpath)
    # ѭ�����������base64������base64����д��ruiyin.cfg
    with open(packge, "r") as f:
        for line in f.readlines():
            line = line.strip('\n')  # ȥ���б���ÿһ��Ԫ�صĻ��з�
            basepackageName = base64.b64encode(line.encode('utf-8'))
            # ��base64����
            flashback = str(basepackageName, 'utf-8')[::-1]
            # д��ruiyin.cfg
            with open(newpath, 'a', encoding='utf-8') as file:
                file.write(flashback + '\n')
                file.close()


if __name__ == '__main__':
    # �ж��Ƿ����ruiyin.cfg
    if os.access(newpath, os.F_OK):
        # ���ڵ���
        writeCfgFlie(newpath)
    else:
        # �����ڵ���
        writeTxtFlie(oldpath)
        # �޸�ruiyin.txtΪruiyin.cfg
        os.rename(oldpath, newpath)
    print('ok')
