# coding=gbk
import base64
import os
import re

import getpass

user_name = getpass.getuser()  # 获取当前用户名
# 未修改的文本路径
packge = 'C:/Users/' + user_name + '/Desktop/com.txt'
oldpath = 'C:/Users/' + user_name + '/Desktop/ruiyin.txt'
# 修改后的文本路径
newpath = 'C:/Users/' + user_name + '/Desktop/ruiyin.cfg'


# 创建txt文件
def create_text(filename):
    path = 'C:/Users/' + user_name + '/Desktop/'
    file_path = path + filename + '.txt'
    file = open(file_path, 'w')
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


# 不存在ruiyin.cfg调用
def writeTxtFlie(oldepath):
    # 创建ruiyin.txt
    create_text('ruiyin')
    # 先清除ruiyin.txt
    oldFile(oldpath)
    # 循环输出包名、base64、倒叙base64，再写入ruiyin.txt
    with open(packge, "r") as f:
        for line in f.readlines():
            line = line.strip('\n')  # 去掉列表中每一个元素的换行符
            basepackageName = base64.b64encode(line.encode('utf-8'))
            # 将base64倒叙
            flashback = str(basepackageName, 'utf-8')[::-1]
            # 写入ruiyin.txt
            with open(oldepath, 'a', encoding='utf-8') as file1:
                file1.write(flashback + '\n')
                file1.close()


# 存在ruiyin.cfg调用
def writeCfgFlie(newpath):
    # 先清除ruiyin.cfg
    newFile(newpath)
    # 循环输出包名、base64、倒叙base64，再写入ruiyin.cfg
    with open(packge, "r") as f:
        for line in f.readlines():
            line = line.strip('\n')  # 去掉列表中每一个元素的换行符
            basepackageName = base64.b64encode(line.encode('utf-8'))
            # 将base64倒叙
            flashback = str(basepackageName, 'utf-8')[::-1]
            # 写入ruiyin.cfg
            with open(newpath, 'a', encoding='utf-8') as file:
                file.write(flashback + '\n')
                file.close()


if __name__ == '__main__':
    # 判断是否存在ruiyin.cfg
    if os.access(newpath, os.F_OK):
        # 存在调用
        writeCfgFlie(newpath)
    else:
        # 不存在调用
        writeTxtFlie(oldpath)
        # 修改ruiyin.txt为ruiyin.cfg
        os.rename(oldpath, newpath)
    print('ok')
