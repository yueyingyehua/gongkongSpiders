# coding:utf8

# Author: tsuki
# Date: 2017-12-10
from unittest import TestCase


# Time: 16:28
from spider.cnnvdSpider import CnnvdSpider


class TestCnnvdSpider(TestCase):
    def test_getUrls(self):
        CnnvdSpider().getUrls()

    def test_getDetailData(self):
        datas = {}
        CnnvdSpider().getDetailData("http://www.cnnvd.org.cn/web/xxk/ldxqById.tag?CNNVD=CNNVD-201712-641", datas)
