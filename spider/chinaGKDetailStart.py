#coding:utf8

#Author: tsuki
#Date: 2017-12-16
#Time: 21:36
import threading

from selenium import webdriver
from selenium.webdriver.support.select import Select

from common.database.dao.gongKongDetailDao import GongKongDetailDao
from spider.chinaGKSpider import ChinaGKSpider


class ChinaGKDetailStart():

    def startSpider(self, url, id, type):
        ChinaGKSpider().getDetail(url, id, type)

    def main(self, type, url):

        #  初始化数据库
        GongKongDetailDao().__init__()

        browser = webdriver.Chrome()
        browser.get(url)
        categroySelect = Select(browser.find_element_by_id("categorySelect_0"))
        thread = []
        i = 0
        for categroy in categroySelect.options:
            if (categroy.text != '-请选择-'):
                i = i + 1
                thread.append(threading.Thread(target=self.startSpider, name=1, args=(url, i, type)))

        j = 0
        while (j < i):
            thread[j].start()
            j = j + 1

        k = 0
        while (k < i):
            thread[k].join()
            k = k + 1

if __name__ == '__main__':
    # type = "DCS"
    # url = "http://www.gongkong.com/ProductChannelnew/ProductCompare?mids=190665&categoryId=652"

    # url = "http://www.gongkong.com/ProductChannelnew/ProductCompare?mids=973411&s=0&sID=&f=0&hid=&categoryId=808"
    # type = "PLC"

    type = "PAC"
    url = "http://www.gongkong.com/ProductChannelnew/ProductCompare?mids=237879&categoryId=917"

    ChinaGKDetailStart().main(type, url)