# coding:utf8

# Author: tsuki
# Date: 2017-12-09
from unittest import TestCase


# Time: 22:59
from spider.urlKeyWordSpider import UrlKeyWordSpider


class TestUrlKeyWordSpider(TestCase):
    def test_getUrlsByBaidu(self):
        # UrlKeyWordSpider().getUrlsByBaidu("工控")
        # UrlKeyWordSpider().getUrlsByBaidu("plc")
        # UrlKeyWordSpider().getUrlsByBaidu("工业控制")
        # UrlKeyWordSpider().getUrlsByBaidu("dcs")
        # UrlKeyWordSpider().getUrlsByBaidu("pac")
        UrlKeyWordSpider().getUrlsByBaidu("工控产品")

    def test_getUrlsByGoogle(self):
        # UrlKeyWordSpider().getUrlsByGoogle("plc")
        # UrlKeyWordSpider().getUrlsByGoogle("工业控制")
        # UrlKeyWordSpider().getUrlsByGoogle("dcs")
        # UrlKeyWordSpider().getUrlsByGoogle("pac")
        UrlKeyWordSpider().getUrlsByGoogle("工控产品")
