# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

wd = webdriver.Chrome("D:\pythonProject\chromedriver.exe")
wd.get("https://newbp.yixinfa.cn")
wd.find_element_by_name('username').send_keys("wxl")
wd.find_element_by_name('password').send_keys("wxl123456")
time.sleep(0.5)
wd.find_element_by_xpath("//button[@class = 'el-button el-button--primary el-button--small btn_login']").click()
time.sleep(1)
wd.find_element(By.XPATH,'//span[text()="设备"]').click()
time.sleep(0.5)
wd.find_element(By.XPATH,'//span[text()="设备管理"]').click()
'''
实现方式 一
    先找到所有的tr标签 class为el-table__row的 找到编号为221059207163的索引
    查找所有的a标签 文本为远程控制的 如果找到了索引 就点击  没找到 就不处理
实现方式二
    直接在input输入编号  然后点击搜索 这样筛选项唯一
    查找a标签 文本为远程控制的   直接点击即可
下面代码为实现方式一

注意点 前端可能在数据拿来后对数据做了处理 导致等上面延时过后直接拿元素会出现拿到的元素等使用时不存在  所
以在拿所有的tr元素时必须加上延时 否则处理时会出错  处理的元素页面上不存在
'''
time.sleep(1)
# wd.find_element(By.XPATH,'//li[text()="2"]').click()
num = "321054382421"
time.sleep(1)
selectIndex = -1
trList = wd.find_elements(By.XPATH,'//tr[@class="el-table__row"]')
for index in range(len(trList) ):
    text = trList[index].text
    if text.count(num) > 0 :
        selectIndex = index
        continue
if selectIndex != -1 :
    aList = wd.find_elements(By.XPATH,'//a[text()="远程控制"]')
    aList[selectIndex].click()
time.sleep(1)
# wd.find_element(By.XPATH,'//a[contains(string(), "交")]').click()
# index =
while(True):
    num=random.randint(10, 100)
    num1=random.randint(10, 100)
    inputs=wd.find_elements(By.XPATH, '//input[@class="el-input__inner"]')
    inputs[0].clear()
    inputs[1].clear()
    inputs=wd.find_elements(By.XPATH, '//input[@class="el-input__inner"]')
    inputs[0].send_keys(num)
    inputs[1].send_keys(num1)
    wd.find_element(By.XPATH, '//a[contains(string(),"交")]').click()
    time.sleep(6)
# print(element_keyword)
