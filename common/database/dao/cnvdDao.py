#coding:utf8

#Author: tsuki
#Date: 2017-12-08
#Time: 22:17
from common.database.dao.mysqlSQLAlchemyBaseDao import MysqlSQLAlchemyBaseDao
from common.database.entity.cnvdEntity import CNVDEntity


class CNVDDao(MysqlSQLAlchemyBaseDao):

    def insert(self, messageResult):
        try:
            cnvd = CNVDEntity(chname = messageResult['chname'],
                        cnvd_id = messageResult['cnvd_id'],
                        cve_id = messageResult['cve_id'],
                        finder = messageResult['finder'],
                        impact_product = messageResult['impact_product'],
                        included_time = messageResult['included_time'],
                        release_time = messageResult['release_time'],
                        reference_link = messageResult['reference_link'],
                        submission_time = messageResult['submission_time'],
                        update_time = messageResult['update_time'],
                        validation_info = messageResult['validation_info'],
                        vendor_patch = messageResult['vendor_patch'],
                        vul_attachment = messageResult['vul_attachment'],
                        vul_description = messageResult['vul_description'],
                        vul_level = messageResult['vul_level'],
                        vul_solution = messageResult['vul_solution'],
                        vul_type = messageResult['vul_type'],
                        bugtraq_id = messageResult['bugtraq_id']
                        )
            self.session.add(cnvd)
            self.session.commit()
        except Exception as excep:
            self.logger.error("insert error {}".format(excep))
            self.session.rollback()
            raise
        self.session.close()

    def selectByCNVDId(self, cnvdId):
        return self.session.query(CNVDEntity).filter_by(cnvd_id = cnvdId).all()




