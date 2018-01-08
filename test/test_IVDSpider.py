# coding:utf8

# Author: tsuki
# Date: 2018-01-06
from unittest import TestCase


# Time: 17:06
from spider.ivdSpider import IVDSpider


class TestIVDSpider(TestCase):
    def test_getUrls(self):
        IVDSpider().getUrls(1)

    def test_getDate(self):
        IVDSpider().getData("http://ivd.winicssec.com/index.php/Home/Detail/index/id/7ad47499-bdfc-4ebc-abe2-88ed69c51bae.html")

    def test_spiderAll(self):
        IVDSpider().spiderAll()