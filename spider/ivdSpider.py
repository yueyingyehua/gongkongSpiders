#coding:utf8

#Author: tsuki
#Date: 2018-01-06
#Time: 16:35
import bs4
import re

from common.config.config import Config
from common.database.dao.ivdDao import IVDDao
from common.log.MyLog import MyLog
from spider.spiderUtil import SpiderUtil


class IVDSpider():
    def __init__(self):
        self.header = Config().getHeader()
        self.logger = MyLog().getLogger()
        self.ivdDao = IVDDao()

    def getUrls(self, num):
        urls = []
        start_url = "http://ivd.winicssec.com/index.php/Home/Index/index/p/" + str(num) + ".html"
        soup = SpiderUtil().getSoup(start_url)

        results = soup.find('div', class_='table_blo').tbody
        for result in results:
            if type(result) == bs4.element.Tag:
                url = "http://ivd.winicssec.com" + result.td.a['href']
                urls.append(url)
            # urls.append(result)
            # urls.append(result.tr.td.a['href'])
        return urls

    def getData(self, url):
        soup = SpiderUtil().getSoup(url)
        data = {}
        data['detail_url'] = url
        chname = soup.find('div', class_="page-header").getText()
        data["chname"] = re.sub("(\t|\n|\r|\040)*", "",chname)
        results = soup.findAll('div', class_="panel panel-success")
        for result in results:
            tag = []
            for content in result.contents:
                if type(content) == bs4.Tag:
                    tag.append(content)
            if len(tag) == 2:
                if tag[0].getText() == "漏洞参数":
                    for p in tag[1].contents:
                        if type(p) == bs4.Tag:
                            text = p.getText().split(":")
                            if len(text) > 0 and text[0] in Config().getIVDVulList():
                                data[Config().getIVDVulList()[text[0]]] = text[1]
                elif tag[0].getText() in Config().getIVDVulList():
                    data[Config().getIVDVulList()[tag[0].getText()]] = re.sub("(\t|\n|\r|\040)*", "", tag[1].getText())
        self.ivdDao.insert(data)

    def spiderAll(self):
        soup = SpiderUtil().getSoup("http://ivd.winicssec.com/index.php/Home/Index/index/p/1.html")
        pageNum = soup.find("a", class_="end").getText()
        for i in range(1, int(pageNum) + 1):
            urls = self.getUrls(i)
            for url in urls:
                self.getData(url)



