#coding:utf8

#Author: tsuki
#Date: 2017-11-14
#Time: 15:37

#日志相关功能接口
import datetime
import logging



class MyLog():
    def getLogger(self):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(str(datetime.date.today()) + ".log")
        fh.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger
