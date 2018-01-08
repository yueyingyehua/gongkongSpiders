#coding:utf8

#Author: tsuki
#Date: 2017-12-09
#Time: 15:17
import urllib

import time

from bs4 import BeautifulSoup
from selenium import webdriver

from common.config.config import Config
from common.database.dao.urlKeyWordDao import UrlKeyWordDao
from common.log.MyLog import MyLog

# 使用搜索引擎搜索关于工控的网站，将页面中的url爬取下来
from spider.spiderUtil import SpiderUtil


class UrlKeyWordSpider():
    def __init__(self):
        self.header = Config().getHeader()
        self.logger = MyLog().getLogger()
        self.urlKeyWordDao = UrlKeyWordDao()

    def getUrlsByBaidu(self, keyWord):
        datas = []
        # 对url中中文处理
        url = "/s?wd=" + urllib.parse.quote(keyWord)
        self.getByBaidu(url, keyWord, datas)
        self.urlKeyWordDao.insert(datas)

    def getUrlsByGoogle(self, keyWord):
        datas = []
        # 对url中中文处理
        start_url = "https://www.google.com.hk/search?q=" + urllib.parse.quote(keyWord)
        browser = webdriver.Chrome()
        browser.get(start_url)
        while (self.isElementExist(browser, '下一页')):
            browser.find_element_by_link_text('下一页').click()
            soup = BeautifulSoup(browser.page_source, "html.parser", from_encoding='UTF-8')
            self.getDataByGoogle(soup, keyWord, datas)
            time.sleep(Config().getSleepTime())
        browser.close()
        self.urlKeyWordDao.insert(datas)

    def getDataByGoogle(self, soup, keyWord, datas):
        results = soup.findAll('div', class_='rc')
        for result in results:
            try:
                data = {}
                data['url'] = result.find('cite', class_='_Rm').getText()
                data['urlTitle'] = result.h3.getText()
                data['searchEngine'] = "Google"
                data['searchWord'] = keyWord
                datas.append(data)
            except Exception as e:
                self.logger.error("getData获取数据错误：[error]:{}……result:{}"
                                  .format(e, str(result).replace(u'\xa0', u' ')))

    def getByBaidu(self, url, keyWord, datas):
        url = "https://www.baidu.com" + url
        soup = SpiderUtil().getSoup(url)

        self.getDataByBaidu(soup, keyWord, datas)

        nextUrl = self.getNextPageUrl(soup)

        if nextUrl != -1:
            self.getByBaidu(nextUrl, keyWord, datas)

    def getDataByBaidu(self, soup, keyWord, datas):
        results = soup.findAll('div', class_="f13")
        for result in results:
            try:
                data = {}
                data['url'] = result.a.getText()
                data['urlTitle'] = result.div['data-tools']
                data['searchEngine'] = "百度"
                data['searchWord'] = keyWord
                datas.append(data)
            except Exception as e:
                self.logger.error("getData获取数据错误：[error]:{}……result:{}"
                                  .format(e, str(result).replace(u'\xa0', u' ')))

    def getNextPageUrl(self, soup):
        nextUrls = soup.find('div', id='page').findAll('a')
        if nextUrls == None:
            return -1
        if len(nextUrls) <= 0:
            return -1
        if nextUrls[len(nextUrls) - 1].getText() != '下一页>':
            return -1
        return nextUrls[len(nextUrls) - 1]['href']

    #判断是否存在此标签
    def isElementExist(self, browser, element):
        flag = True
        try:
            browser.find_element_by_link_text(element)
        except:
            flag = False
        return flag