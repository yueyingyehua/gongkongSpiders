#coding:utf8

#Author: tsuki
#Date: 2018-01-06
#Time: 16:38
import sqlalchemy

from common.config.mysqlConfig import MysqlConfig


class IVDEntity(MysqlConfig().getBaseModel()):
    __tablename__ = "ivd"
    __table_args__ = {
        "mysql_charset": "utf8"
    }

    id = sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True)
    chname = sqlalchemy.Column('chname', sqlalchemy.String(255), nullable=False, server_default='')
    cve_id = sqlalchemy.Column('cve_id', sqlalchemy.String(255), nullable=False, server_default='')
    cnvd_id = sqlalchemy.Column('cnvd_id', sqlalchemy.String(255), nullable=False, server_default='')
    cnnvd_id = sqlalchemy.Column('cnnvd_id', sqlalchemy.String(255), nullable=False, server_default='')
    vul_level = sqlalchemy.Column('vul_level', sqlalchemy.String(255), nullable=False, server_default='')
    release_time = sqlalchemy.Column('release_time', sqlalchemy.TIMESTAMP(), nullable=False,
                                     server_default='1970-01-02 00:00:00')
    impact_product = sqlalchemy.Column('impact_produce', sqlalchemy.Text(), nullable=False)
    vul_description = sqlalchemy.Column('vul_description', sqlalchemy.Text(), nullable=False)
    vul_solution = sqlalchemy.Column('vul_solution', sqlalchemy.Text(), nullable=False)
    detail_url= sqlalchemy.Column('detail_url', sqlalchemy.Text(), nullable=False)

