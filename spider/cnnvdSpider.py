#coding:utf8

#Author: tsuki
#Date: 2017-12-10
#Time: 16:11
import re

import bs4

from common.config.config import Config
from common.database.dao.cnnvdDao import CnnvdDao
from common.log.MyLog import MyLog
from spider.spiderUtil import SpiderUtil


class CnnvdSpider():
    def __init__(self):
        self.header = Config().getHeader()
        self.logger = MyLog().getLogger()
        self.cnnvdDao = CnnvdDao()

    def spiderAll(self,):
        start_url = "http://www.cnnvd.org.cn/web/vulnerability/querylist.tag"
        urls = self.getUrls(start_url)
        for url in urls:
            data = self.getDetailData(url)
            self.cnnvdDao.insert(data)

    def getUrls(self, start_url):
        urls = []
        soup = SpiderUtil().getSoup(start_url)

        page = self.getTotalPage(soup)

        #倒序爬取，即从最后一页开始爬取
        for i in range(page):
            self.getDetailUrls(i, urls)
        return urls

    def getTotalPage(self, soup):
        # 获取总条数
        pageText = soup.find('div', class_='page').getText().split("\n")
        totalNum = 0
        for text in pageText:
            if text != '':
                totalNum = int(re.sub("\D", "", text))
                break
        if totalNum == 0:
            self.logger.error("getTotalNum Error")

        if totalNum % 10 != 0:
            page = int(totalNum / 10 + 1)
        else:
            page = int(totalNum / 10)
        return page

    def getDetailUrls(self, page, urls):
        url = "http://www.cnnvd.org.cn/web/vulnerability/querylist.tag?pageno=" + str(page)
        soup = SpiderUtil().getSoup(url)

        list_list = soup.find('div', class_='list_list')
        urlList = list_list.findAll('div', class_='f1')
        for u in urlList:
            urls.append(u.a['href'])

    def getDetailData(self, url):
        data = {}
        data['detailUrl'] = url
        soup = SpiderUtil().getSoup(url)
        details = soup.find('div', class_='detail_xq w770')
        data['chname'] = details.h2.getText()
        for li in details.ul:
            if type(li) == bs4.element.Tag:
                texts = re.sub("(\t|\n|\r|\040)*", "", li.getText()).split("：")
                if texts[0] in Config().getCnnvdVulList():
                    codeName = Config().getCnnvdVulList()[texts[0]]
                    data[codeName] = texts[1]
                    print(codeName + ": " + data[codeName])
        #漏洞简介
        vul_descriptions = soup.find('div', class_='d_ldjj').findAll('p', style='text-indent:2em')
        data['vul_description'] = ''
        for vul_description in vul_descriptions:
            data['vul_description'] += re.sub("(\t|\n|\r|\040)*", "", vul_description.getText())
        #漏洞公告，参考网址，受影响实体
        contents = soup.findAll('div', class_='d_ldjj m_t_20')
        for content in contents:
            title = content.find('div', class_='title_bt').getText()
            title = re.sub("(\t|\n|\r|\040)*", "", title)
            if title in Config().getCnnvdVulList():
                codeName = Config().getCnnvdVulList()[title]
                data[codeName] = ''
                p = content.findAll('p', style='text-indent:2em')
                for x in p:
                    data[codeName] += re.sub("(\t|\n|\r|\040)*", "", x.getText())
        return data







