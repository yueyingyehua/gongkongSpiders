#coding:utf8

#Author: tsuki
#Date: 2017-12-08
#Time: 15:49
import urllib
from urllib import request

from bs4 import BeautifulSoup

from common.config.config import Config
from common.log.MyLog import MyLog
from common.webDriver import Webdriver


class SpiderUtil():

    def __int__(self):
        self.logger = MyLog().getLogger()

    def getSoup(self, url):
        req = request.Request(url, headers=Config().getHeader())
        for i in range(Config().getMAX_NUM()):
            try:
                resp = request.urlopen(req)
            except urllib.error.URLError as e:
                if i < Config().getMAX_NUM() - 1:
                    continue
                else:
                    self.logger.error("{}:{}:次之后还是失败".format(url, Config().getMAX_NUM()))
                    return

        content = resp.read()
        soup = BeautifulSoup(content, "html.parser", from_encoding='utf-8')
        return soup

    def getSoupByWebDriver(self, url):
        content = Webdriver().getPage_source(url)
        soup = BeautifulSoup(content, "html.parser", from_encoding='UTF-8')
        Webdriver().close()
        return soup