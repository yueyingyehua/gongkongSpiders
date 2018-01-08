#coding:utf8

#Author: tsuki
#Date: 2017-12-13
#Time: 21:13
import re

from common.config.config import Config
from common.database.dao.urlKeyWordDao import UrlKeyWordDao
from common.log.MyLog import MyLog


class KeyWordAnalyst():
    def __init__(self):
        self.header = Config().getHeader()
        self.logger = MyLog().getLogger()
        self.urlKeyWordDao = UrlKeyWordDao()

    def dataPreparation(self):
        dataCount = {}
        dataList = self.urlKeyWordDao.listURL()
        pattern = re.compile(Config().getFilterFile())
        for data in dataList:
            datas = data.url.split(".")
            for key in datas:
                match = pattern.match(key)
                if match == None and key != '':
                    if not dataCount.get(key):
                        dataCount[key] = 1
                    else:
                        dataCount[key] += 1
        sort = sorted(dataCount.items(), key=lambda e:e[1], reverse=True)
        for item in sort:
            print(item)
            self.logger.debug(item)


    def dataPreparationXXX(self):
        dataCount = {}
        dataList = self.urlKeyWordDao.listURL()
        pattern = re.compile(Config().getFilterFile2())
        for data in dataList:
            datas = data.url.split("/")
            for key in datas:
                match = pattern.match(key)
                if match == None and key != '':
                    if not dataCount.get(key):
                        dataCount[key] = 1
                    else:
                        dataCount[key] += 1
        sort = sorted(dataCount.items(), key=lambda e:e[1], reverse=True)
        for item in sort:
            print(item)
            self.logger.debug(item)

    def dataPreparationByEngine(self, engine):
        dataList = self.urlKeyWordDao.listURLByEngine(engine)
        self.xx(dataList)

    def dataPreparationBySearchWord(self, searchWord):
        dataList = self.urlKeyWordDao.listURLBySearchWord(searchWord)
        self.xx(dataList)


    def xx(self, dataList):
        dataCount = {}
        pattern = re.compile(Config().getFilterFile2())
        for data in dataList:
            datas = data.url.split("/")
            for key in datas:
                match = pattern.match(key)
                if match == None and key != '':
                    if not dataCount.get(key):
                        dataCount[key] = 1
                    else:
                        dataCount[key] += 1
        sort = sorted(dataCount.items(), key=lambda e: e[1], reverse=True)
        for item in sort:
            print(item)
            self.logger.debug(item)

# KeyWordAnalyst().dataPreparationXXX()
# KeyWordAnalyst().dataPreparationBySearchWord("pac")
KeyWordAnalyst().dataPreparation()
