#coding:utf8

#Author: tsuki
#Date: 2017-12-09
#Time: 13:48
import os

import time
from selenium import webdriver


class Webdriver():

    # 初始化并加载浏览器
    def __init__(self):
        # 获取当前目录
        path = os.getcwd()
        executable_path = path + "\\chromedriver.exe"
        print(executable_path)
        self.browser = webdriver.Chrome(executable_path)


    # 获取页面
    def getPage_source(self, url):
        self.browser.get(url)
        # 刷新页面获取完整的页面
        self.browser.refresh()
        time.sleep(0.3)
        return self.browser.page_source

    # 获取cookie
    def getCookies(self, url):
        self.browser.get(url)
        # 刷新页面  重新加载页面
        self.browser.refresh()
        time.sleep(0.3)
        res = self.browser.get_cookies()
        # (list)res = [{'domain': 'www.cnvd.org.cn', 'httpOnly': True, 'expiry': 1527519798.543155, 'secure': False, 'value': '1c652993f3cfb95e68057050a70b69ef', 'name': '__jsluid', 'path': '/'}, {'domain': 'www.cnvd.org.cn', 'httpOnly': False, 'expiry': 1495987361, 'secure': False, 'value': '1495983761.518|0|lKyWZPLs%2FizLz8vTlbysQtasKFw%3D', 'name': '__jsl_clearance', 'path': '/'}]
        cookie = ""
        for r in res:
            cookie += (r['name'] + "=" + r["value"] + ";")
        return cookie

    def close(self):
        self.browser.close()
