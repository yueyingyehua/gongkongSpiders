#coding:utf8

#Author: tsuki
#Date: 2017-12-08
#Time: 15:31
import logging

from common.database.dao.mysqlSQLAlchemyBaseDao import MysqlSQLAlchemyBaseDao
from common.database.entity.gongKongDCSEntity import GongKongDCSEntity
from common.database.entity.gongKongEntity import GongKongEntity
from common.database.entity.gongKongPACEntity import GongKongPACEntity
from common.database.entity.gongKongPCLEntity import GongKongPLCEntity
from common.database.entity.gongKongURLEntity import GongKongURLEntity


class GongKongDao(MysqlSQLAlchemyBaseDao):

    def insert(self, messageResult, uuidURL):
        try:
            gongkong = GongKongEntity(productName = messageResult['productName'],
                                      keyWord = messageResult['keyWord'],
                                      produceCategory = messageResult['produceCategory'],
                                      brand = messageResult['brand'],
                                      produceInfo = messageResult['produceInfo'],
                                      detailsLinkUid = uuidURL
                                      )
            self.session.add(gongkong)
            self.session.commit()
        except Exception as excep:
            self.session.rollback()
            raise
        self.session.close()

    def insertURL(self, detailsLink, uuid):
        try:
            gongkongURl = GongKongURLEntity(detailsLink = detailsLink,
                                            uuid = uuid)
            self.session.add(gongkongURl)
            self.session.commit()
            flag = True
        except Exception as excep:
            self.session.rollback()
            #记录exception
            self.logger.error("详情页url(" + detailsLink +")插入失败：" + str(excep))
            flag = False
        self.session.close()
        return flag

    def getOne(self, url):
        return self.session.query(GongKongURLEntity).filter_by(detailsLink = url).all()

    def insertDetail(self, detail, type):
        try:
            # for detail in details:
            if type == 'PLC':
                gongKongDetail = GongKongPLCEntity(categroy = detail['categroy'],
                                                   brand = detail['brand'],
                                                   product = detail['product'],
                                                   model = detail['model'])
            elif type == 'DCS':
                gongKongDetail = GongKongDCSEntity(categroy = detail['categroy'],
                                                   brand = detail['brand'],
                                                   product = detail['product'],
                                                   model = detail['model'])
            elif type == 'PAC':
                gongKongDetail = GongKongPACEntity(categroy = detail['categroy'],
                                                   brand = detail['brand'],
                                                   product = detail['product'],
                                                   model = detail['model'])

            self.session.add(gongKongDetail)
            self.session.commit()
        except Exception as excep:
            self.session.rollback()
            self.logger.error("插入失败: " + detail['categroy'])
            raise
        self.session.close()

