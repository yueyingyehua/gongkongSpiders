#coding:utf8

#Author: tsuki
#Date: 2017-12-05
#Time: 15:42
import re


class Config:
    __user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"
    __accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    __accept_Encoding = "gzip, deflate, sdch"
    __accept_Language = "zh-CN,zh;q=0.8"
    __header = {"User-Agent": __user_agent, "Accept-Language": __accept_Language,
              "Accept_Encoding": __accept_Encoding, "Accept": __accept}

    __cnvdVulList = {
        "chname": 'chname',
        "CNVD-ID": "cnvd_id",
        "发布时间": "release_time",
        "危害级别": "vul_level",
        "影响产品 ": "impact_product",
        "BUGTRAQ ID": "bugtraq_id",
        "CVE ID": "cve_id",
        "漏洞描述": "vul_description",
        "漏洞类型": "vul_type",
        "参考链接": "reference_link",
        "漏洞解决方案": "vul_solution",
        "漏洞发现者": "finder",
        "厂商补丁": "vendor_patch",
        "验证信息": "validation_info",
        "报送时间": "submission_time",
        "收录时间": "included_time",
        "更新时间": "update_time",
        "漏洞附件": "vul_attachment",
    }

    __cnnvdVulList = {
        "漏洞名称": 'chname',
        "CNNVD编号": "cnnvd_id",
        "危害等级": "vul_level",
        "CVE编号": "cve_id",
        "漏洞类型": "vul_type",
        "发布时间": "release_time",
        "更新时间": "update_time",
        "威胁类型": "Threat_type",
        "厂商": "company",
        "漏洞来源": "source_of_vul",
        "漏洞简介": "vul_description",
        "漏洞公告": "vul_announcement",
        "参考网址": "reference_link",
        "受影响实体": "affected_entity"
    }

    __ivdVulList = {
        "漏洞类型": "vul_type",
        "危险级别": "vul_level",
        "CVE编号": "cve_id",
        "CNVD编号": "cnvd_id",
        "CNNVD编号": "cnnvd_id",
        "发布时间": "release_time",
        "受影响的平台和产品": "impact_product",
        "漏洞描述": "vul_description",
        "安全建议&解决方案": "vul_solution"

    }

    __filterField = [
        "www",
        "com",
        "\\xa0",
        "html",
        "bbs",
        "https",
        "http",
        "net",
        "cn",
        "org",
        "php",
        "/",
        "aspx"
    ]

    __filterField2 = [
        "https",
        "\\xa0",
        "http",
        "html",
    ]



    __MAX_NUM = 10

    __SLEEPTIME = 0.5

    def getHeader(self):
        return self.__header

    def getMAX_NUM(self):
        return self.__MAX_NUM

    def getSleepTime(self):
        return self.__SLEEPTIME

    def getCnvdVulList(self):
        return self.__cnvdVulList

    def getCnnvdVulList(self):
        return self.__cnnvdVulList

    def getIVDVulList(self):
        return self.__ivdVulList

    def getFilterFile(self):
        return "|".join(self.__filterField)

    def getFilterFile2(self):
        return "|".join(self.__filterField2)


# pattern = re.compile(Config().getFilterFile())
# s = "www4tdgdsfgsdfghttpshttp/"
# match = pattern.match(s)
# if match:
#     print(match.group())
