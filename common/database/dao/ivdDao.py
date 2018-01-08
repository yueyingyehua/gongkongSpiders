#coding:utf8

#Author: tsuki
#Date: 2018-01-06
#Time: 16:37
from common.database.dao.mysqlSQLAlchemyBaseDao import MysqlSQLAlchemyBaseDao
from common.database.entity.ivdEntity import IVDEntity


class IVDDao(MysqlSQLAlchemyBaseDao):

    def insert(self, ivd):
        try:
            ivdEntity = IVDEntity(chname = ivd['chname'],
                                  cve_id = ivd['cve_id'],
                                  cnvd_id = ivd['cnvd_id'],
                                  cnnvd_id = ivd['cnnvd_id'],
                                  vul_level = ivd['vul_level'],
                                  release_time = ivd['release_time'],
                                  impact_product = ivd['impact_product'],
                                  vul_description = ivd['vul_description'],
                                  vul_solution = ivd['vul_solution'],
                                  detail_url = ivd['detail_url'])
            self.session.add(ivdEntity)
            self.session.commit()
        except Exception as excep:
            self.logger.error("insert error {}".format(excep))
            self.session.rollback()
            raise
        self.session.close()
