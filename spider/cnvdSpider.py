#coding:utf8

#Author: tsuki
#Date: 2017-12-08
#Time: 16:09
import bs4
import re
from bs4 import BeautifulSoup
from pymysql import NULL
from common.config.config import Config
from common.database.dao.cnvdDao import CNVDDao
from common.log.MyLog import MyLog
from common.webDriver import Webdriver
from spider.spiderUtil import SpiderUtil


# 爬取cnvd中的工控漏洞

class CNVDSpider():
    def __init__(self):
        self.header = Config().getHeader()
        self.logger = MyLog().getLogger()
        self.cnvdDao = CNVDDao()

    def getUrls(self, num):
        urls = []
        self.logger.info("开始页面{}".format(num))
        start_url = "http://ics.cnvd.org.cn/?max=20&offset="+str(num)

        soup = SpiderUtil().getSoup(start_url)

        results = soup.findAll('td', style="text-align:left;padding-left:10px;")
        self.logger.info("{} 页面获取到的url个数：{}".format(start_url, len(results)))
        for result in results:
            urls.append(result.a['href'])

        return urls

    def getData(self, url):
        soup = SpiderUtil().getSoupByWebDriver(url)

        print(url)
        chname = soup.find('div', class_='blkContainerSblk').h1.getText()
        messageResult = {}
        messageResult['chname'] = chname
        tbody = soup.findAll("table", class_="gg_detail")[0].tbody

        TRlist = tbody.findAll('tr')
        for trlist in TRlist:
            if trlist.td.string == "影响产品":
                impact_productSum = ''
                if "影响产品" not in messageResult:
                    messageResult["impact_product"] = []
                for td in trlist.td.next_siblings:
                    if type(td) == bs4.element.Tag:
                        for k in td:
                            impact_product = ''
                            if type(k) == bs4.element.Tag:
                                impact_product = re.sub("(\t|\n|\r|\040)*", "", k.getText())
                            else:
                                impact_product = re.sub("(\t|\n|\r|\040)*", "", k.string)
                            if impact_product != "":
                                if impact_productSum == '':
                                    impact_productSum = impact_product
                                else:
                                    impact_productSum = impact_productSum + ',' + impact_product

                messageResult['impact_product'].append(impact_productSum)
            else:
                name = trlist.td.string;
                if name in Config().getCnvdVulList():
                    codename = Config().getCnvdVulList()[name]
                    for td in trlist.td.next_siblings:
                        if type(td) == bs4.element.Tag:
                            tdText = re.sub(r"(\r|\t|\n|\040)*", "", td.getText())
                            if len(tdText):
                                if codename in messageResult:
                                    messageResult[codename].append(tdText)
                                else:
                                    messageResult[codename] = tdText
                else:
                    self.logger.warning("url:{}, Chname:{}。 未收入的标签：{}".format(url, chname, name))
        for name in Config().getCnvdVulList():
            if Config().getCnvdVulList()[name] not in messageResult:
                messageResult[Config().getCnvdVulList()[name]] = NULL
        self.cnvdDao.insert(messageResult)

    # 判断是否是已经爬过的信息
    # 即判断cnvd-id是否存在
    def isExist(self, cnvd_id):
        list = self.cnvdDao.selectByCNVDId(cnvd_id)
        if len(list) == 1:
            return True  # 表示存在该条信息
        elif len(list) == 0:
            return False  # 表示不存在该条信息
        else:
            self.logger.error("查询出错：cnvd_id:{}, [ERROR]:list:{}".format(cnvd_id, list))
            return

    def getPageNum(self):
        soup = SpiderUtil().getSoupByWebDriver("http://ics.cnvd.org.cn/")
        step = soup.findAll("a", class_="step")
        pageNum = step[len(step)-1].get_text()
        return int(pageNum)

    # 爬取全部信息
    def spiderAll(self):
        pageNum = self.getPageNum()
        # 从最后一页开始爬取
        for i in range(pageNum)[::-1]:
            urls = self.getUrls((i- 1) * 20)
            for url in urls:
                u = url.split("/")
                cnvdId = u[len(u) - 1]
                if self.isExist(cnvdId) == False:
                    try:
                        self.getData(url)  # 不存在该信息则获取并插入
                    except Exception as excep:
                        self.logger.error("getDataError{}".format(excep))

    # 更新数据
    def update(self):
        pageNum = self.getPageNum()
        # 从第一页开始更新数据
        for i in range(pageNum):
            urls = self.getUrls(i * 20)
            for url in urls:
                u = url.split("/")
                cnvdId = u[len(u) - 1]
                if self.isExist(cnvdId) == False:
                    try:
                        self.getData(url)  # 不存在该信息则获取并插入
                    except Exception as excep:
                        self.logger.error("getDataError{}".format(excep))
                elif self.isExist(cnvdId) == True:
                    return  # 存在该信息 则退出



# 存在的问题：如果在未更新完的情况下程序被终止时才重新运行更新数据 这会丢失中间的一些数据