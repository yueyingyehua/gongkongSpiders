#coding:utf-8

import re
import uuid
from datetime import time

import bs4
from selenium import webdriver
from selenium.webdriver.support.select import Select

from common.config.config import Config
from common.database.dao.gongKongDao import GongKongDao
from common.log.MyLog import MyLog
from spider.spiderUtil import SpiderUtil


# 爬取工控产品信息以及具体型号
class ChinaGKSpider():
    def __init__(self):
        self.header = Config().getHeader()
        self.logger = MyLog().getLogger()
        self.gongKongDao = GongKongDao()

    def getUrls(self, page):
        urls = []
        start_url = "http://www.gongkong.com/select/QueryLink?pageIndex=" + str(page) + "&articleForm=productInfo"

        soup = SpiderUtil().getSoup(start_url)
        result = soup.findAll("div", class_ = "main_r_text")

        print(start_url, " 页面获取到的url个数: ", len(result))
        self.logger.info(start_url + " 页面获取到的url个数: " + str(len(result)))
        for i in result:
            urls.append(i.a['href'])
        return urls

    def getData(self, url):
        datas = {}
        datas['detailsLink'] = url
        detailsLink = url;

        uuidURL = str(uuid.uuid1())

        # 此处进行查找url数据库，如果不存在则进行解析，否则则返回
        if (len(self.gongKongDao.getOne(detailsLink)) == 0):
            self.gongKongDao.insertURL(detailsLink, uuidURL)
            soup = SpiderUtil().getSoup(url)

            tab_text = soup.find("div", class_="tab_text")

            if (tab_text == None):
                datas['productName'] = soup.find('div', class_='product_title').h1.getText()
                table = soup.find('table', class_='dqfs1')
                for tr in table.children:
                    if type(tr) == bs4.element.Tag:
                        for td in tr.children:
                            if type(td) == bs4.element.Tag:
                                if td.string == '关键字：':
                                    for t in td.next_siblings:
                                        if type(t) == bs4.element.Tag:
                                            datas['keyWord'] = t.getText().strip().replace("\n", "&&")
                                            # print("关键字：" + keyWord)
                                elif td.string == '产品分类：':
                                    for t in td.next_siblings:
                                        if type(t) == bs4.element.Tag:
                                            datas['produceCategory'] = t.getText().strip().replace("\040", "&&")
                                            # print("产品分类：" + produceCategory)
                                elif td.string == '品牌：':
                                    for t in td.next_siblings:
                                        if type(t) == bs4.element.Tag:
                                            datas['brand'] = re.sub("(\t|\n|\r|\040)*", "", t.getText())
                                            # print("品牌：" + brand)
                datas['produceInfo'] = soup.find('dd', style='overflow: auto; line-height: 22px;').getText()
                # print("产品简介: " + productInfo)
            else:
                # 当时只有title的时候将其title拆成品牌，产品名，分类
                # 如：'http://www.gongkong.com/ProductSeriesNew/Detail?id=31223&categoryId=808'
                for tab in tab_text.children:
                    if type(tab) == bs4.element.Tag:
                        te = re.sub("(\040)*", "", tab.getText())
                        tes = te.split("\xa0\xa0") #\xa0是&nbsp的转义字符  使用repr()打印出来的
                        brand = tes[0]
                        productName = tes[1]
                        produceCategory = tes[2]
                        datas['brand'] = brand
                        datas['productName'] = productName
                        datas['produceCategory'] = produceCategory
                        print("产品名字：" + productName)
                        print("产品分类：" + produceCategory)
                        print("品牌：" + brand)
            self.gongKongDao.insertGongKong(datas, uuidURL)

    # 获取具体的型号
    def getDetail(self, url, id, type):
        detail = {}

        # 非编译器运行时
        # path = os.getcwd()
        # executable_path = path + "\\chormedirver.exe"
        # print(executable_path)
        # browser = webdriver.Chrome(executable_path)

        browser = webdriver.Chrome()
        browser.get(url)
        categroySelect = Select(browser.find_element_by_id("categorySelect_0"))
        categroy = categroySelect.options[id].text
        if(categroy != '-请选择-'):
            detail['categroy'] = categroy
            categroySelect.select_by_visible_text(categroy.strip())
            time.sleep(Config.getSleepTime())
            brandSelect = Select(browser.find_element_by_id("brandSelect_0"))
            for brand in brandSelect.options:
                if (brand.text != '-请选择-'):
                    #浏览器选择
                    detail['brand'] = brand.text
                    brandSelect.select_by_visible_text(brand.text)
                    time.sleep(Config.getSleepTime())
                    productSelect = Select(browser.find_element_by_id("ProductSelect_0"))
                    for product in productSelect.options:
                        if (product.text != '-请选择-'):
                            detail['product'] = product.text
                            #浏览器选择
                            productSelect.select_by_visible_text(product.text)
                            time.sleep(Config.getSleepTime())
                            modelSelect = Select(browser.find_element_by_id("modelSelect_0"))
                            # 存储全部选择
                            for model in modelSelect.options:
                                if (model.text != '-请选择-'):
                                    detail['model'] = model.text
                                    # details.append(detail)
                                    print("类别： " + detail['categroy'] + " 品牌：" + detail['brand'] + " 系列：" + detail['product'] + " 型号：" + detail['model'])
                                    self.gongKongDao.insertDetail(detail, type)
        browser.close()









