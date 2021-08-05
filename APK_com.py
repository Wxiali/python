# content of test_APK_com.py
# coding=gbk
import base64
import multiprocessing
import os
import re
import getpass
import sys
import time

user_name = getpass.getuser()  # 获取当前用户名
# 未修改的文本路径
oldpath = 'C:/Users/' + user_name + '/Desktop/ruiyin.txt'
# 修改后的文本路径
newpath = 'C:/Users/' + user_name + '/Desktop/ruiyin.cfg'
# 创建一个AaptLog.txt文本
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


# 创建txt文件
def create_text(filename):
    path = 'C:/Users/' + user_name + '/Desktop/'
    file_path = path + filename + '.txt'
    file = open(file_path, 'w')
    file.close()


# 创建AaptLog.txt文件
def create_aaptLog():
    file = open(aaptLog, 'w')
    file.close()


def oldFile(oldpath):
    # 先清除ruiyin.txt文本
    with open(oldpath, "r+") as f:
        f.seek(0)
        f.truncate()


def newFile(newpath):
    # 清除ruiyin.cfg文本
    with open(newpath, "r+") as f:
        f.seek(0)
        f.truncate()


# 不存在ruiyin.cfg
def writeTxtFlie(oldepath):
    a = packagename_activity()
    # 获取路径
    lujing = "C:\\Users\\" + user_name + "\\Desktop\\apk"
    # 拿到路径下的apk
    li = os.listdir(lujing)
    # 创建ruiyin.txt
    create_text('ruiyin')
    # 先清除ruiyin.txt
    oldFile(oldpath)
    # 循环输出包名、base64、倒叙base64，再写入ruiyin.txt
    for j in li:
        # 获取apk包名
        packageName = a.get_packagename(j)
        nameObj = ''.join(packageName)
        # 获取包名base64
        basepackageName = base64.b64encode(nameObj.encode('utf-8'))
        # 将base64倒叙
        flashback = str(basepackageName, 'utf-8')[::-1]
        # 写入ruiyin.txt
        with open(oldepath, 'a', encoding='utf-8') as file1:
            file1.write(flashback + '\n')
            file1.close()
        continue


# 存在ruiyin.cfg
def writeCfgFlie(newpath):
    a = packagename_activity()
    # 获取路径
    lujing = "C:\\Users\\" + user_name + "\\Desktop\\apk"
    # 拿到路径下的apk
    li = os.listdir(lujing)
    # 先清除ruiyin.cfg
    newFile(newpath)
    # 循环输出包名、base64、倒叙base64，再写入ruiyin.cfg
    for j in li:
        # 获取apk包名
        packageName = a.get_packagename(j)
        nameObj = ''.join(packageName)
        # 获取包名base64
        basepackageName = base64.b64encode(nameObj.encode('utf-8'))
        # 将base64倒叙
        flashback = str(basepackageName, 'utf-8')[::-1]
        # 写入ruiyin.cfg
        with open(newpath, 'a', encoding='utf-8') as file:
            file.write(flashback + '\n')
            file.close()
        continue


if __name__ == '__main__':
    create_aaptLog()
    # 判断是否存在ruiyin.cfg
    if os.access(newpath, os.F_OK):
        # 存在调用
        writeCfgFlie(newpath)
    else:
        # 不存在调用
        writeTxtFlie(oldpath)
        # 修改ruiyin.txt为ruiyin.cfg
        os.rename(oldpath, newpath)
    os.remove(aaptLog)
    print('执行成功，已生成ruiyin.cfg文件')
    time.sleep(2)
