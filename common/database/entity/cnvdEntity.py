#coding:utf8

#Author: tsuki
#Date: 2017-12-08
#Time: 22:33
import sqlalchemy

from common.config.mysqlConfig import MysqlConfig


class CNVDEntity(MysqlConfig().getBaseModel()):
    __tablename__ = "cnvd"
    __table_args__ = {
        "mysql_charset": "utf8"
    }

    id = sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True)
    chname = sqlalchemy.Column("chname", sqlalchemy.String(255), nullable=False, server_default='')
    cnvd_id = sqlalchemy.Column('cnvd_id', sqlalchemy.String(255), nullable=False, server_default='')
    vul_description = sqlalchemy.Column('vul_description', sqlalchemy.Text(), nullable=False)
    vul_solution = sqlalchemy.Column('vul_solution', sqlalchemy.Text(), nullable=False)
    vul_attachment = sqlalchemy.Column('vul_attachment', sqlalchemy.Text(), nullable=False)
    vul_type = sqlalchemy.Column('vul_type', sqlalchemy.String(255), nullable=False, server_default='')
    vul_level = sqlalchemy.Column('vul_level', sqlalchemy.String(255), nullable=False, server_default='')
    cve_id = sqlalchemy.Column('cve_id', sqlalchemy.String(255), nullable=False, server_default='')
    impact_product = sqlalchemy.Column('impact_product', sqlalchemy.Text(), nullable=False)
    validation_info = sqlalchemy.Column('validation_info', sqlalchemy.String(255), nullable=False, server_default='')
    finder = sqlalchemy.Column('finder', sqlalchemy.Text(), nullable=False, server_default='')
    reference_link = sqlalchemy.Column('reference_link', sqlalchemy.Text(), nullable=False)
    vendor_patch = sqlalchemy.Column('vendor_patch', sqlalchemy.Text(), nullable=False)
    update_time = sqlalchemy.Column('update_time', sqlalchemy.TIMESTAMP(), nullable=False,
                                    server_default='1970-01-02 00:00:00')
    included_time = sqlalchemy.Column('included_time', sqlalchemy.TIMESTAMP(), nullable=False,
                                      server_default='1970-01-02 00:00:00')
    submission_time = sqlalchemy.Column('submission_time', sqlalchemy.TIMESTAMP(), nullable=False,
                                        server_default='1970-01-02 00:00:00')
    release_time = sqlalchemy.Column('release_time', sqlalchemy.TIMESTAMP(), nullable=False,
                                     server_default='1970-01-02 00:00:00')
    bugtraq_id = sqlalchemy.Column('bugtraq_id', sqlalchemy.String(255), nullable=False, server_default='')
