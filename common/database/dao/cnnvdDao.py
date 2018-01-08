#coding:utf8

#Author: tsuki
#Date: 2017-12-10
#Time: 15:38
from common.database.dao.mysqlSQLAlchemyBaseDao import MysqlSQLAlchemyBaseDao
from common.database.entity.cnnvdEntity import CnnvdEntity


class CnnvdDao(MysqlSQLAlchemyBaseDao):
    def insert(self, cnnvdEntity):
        try:
            cnnvd = CnnvdEntity(chname = cnnvdEntity['chname'],
                          cnnvd_id = cnnvdEntity['cnnvd_id'],
                          cve_id = cnnvdEntity['cve_id'],
                          release_time = cnnvdEntity['release_time'],
                          update_time = cnnvdEntity['update_time'],
                          vul_level = cnnvdEntity['vul_level'],
                          vul_type = cnnvdEntity['vul_type'],
                          Threat_type = cnnvdEntity['Threat_type'],
                          source_of_vul = cnnvdEntity['source_of_vul'],
                          vul_description = cnnvdEntity['vul_description'],
                          vul_announcement = cnnvdEntity['vul_announcement'],
                          reference_link = cnnvdEntity['reference_link'],
                          affected_entity = cnnvdEntity['affected_entity'],
                          company = cnnvdEntity['company'],
                          detailUrl = cnnvdEntity['detailUrl']
                        )
            self.session.add(cnnvd)
            self.session.commit()
        except Exception as excep:
            self.logger.error("insert error {}".format(excep))
            self.session.rollback()
            raise
        self.session.close()
