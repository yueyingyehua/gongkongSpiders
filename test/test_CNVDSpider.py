# coding:utf8

# Author: tsuki
# Date: 2017-12-09
from unittest import TestCase


# Time: 14:03
from spider.cnvdSpider import CNVDSpider


class TestCNVDSpider(TestCase):
    def test_spiderAll(self):
        CNVDSpider().spiderAll()

    def test_update(self):
        self.fail()
