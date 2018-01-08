#coding:utf8

#Author: tsuki
#Date: 2017-12-16
#Time: 21:38
from common.database.dao.mysqlSQLAlchemyBaseDao import MysqlSQLAlchemyBaseDao
from common.database.entity.gongKongDCSEntity import GongKongDCSEntity
from common.database.entity.gongKongPACEntity import GongKongPACEntity
from common.database.entity.gongKongPCLEntity import GongKongPLCEntity


class GongKongDetailDao(MysqlSQLAlchemyBaseDao):

    def insertGongKongDetail(self, detail, type):
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
            self.logging.error("插入失败: " + detail['categroy'])
            raise
        self.session.close()
