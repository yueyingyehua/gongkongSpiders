#coding:utf8

#Author: tsuki
#Date: 2017-12-08
#Time: 22:37
import sqlalchemy

from common.config.mysqlConfig import MysqlConfig


class CnnvdEntity(MysqlConfig().getBaseModel()):
    __tablename__ = "cnnvd"
    __table_args__ = {
        "mysql_charset": "utf8"
    }

    id = sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True)
    chname = sqlalchemy.Column("chname", sqlalchemy.String(255), nullable=False, server_default='')
    cnnvd_id = sqlalchemy.Column("cnnvd_id", sqlalchemy.String(255), nullable=False, server_default='')
    release_time = sqlalchemy.Column("release_time", sqlalchemy.TIMESTAMP, nullable=False,
                                     server_default='1970-01-02 00:00:00')
    update_time = sqlalchemy.Column("update_time", sqlalchemy.TIMESTAMP, nullable=False,
                                    server_default='1970-01-02 00:00:00')
    vul_level = sqlalchemy.Column("vul_level", sqlalchemy.String(255), nullable=False, server_default='')
    vul_type = sqlalchemy.Column("vul_type", sqlalchemy.String(255), nullable=False, server_default='')
    Threat_type = sqlalchemy.Column("Threat_type", sqlalchemy.String(255), nullable=False, server_default='')
    cve_id = sqlalchemy.Column("cve_id", sqlalchemy.String(255), nullable=False, server_default='')
    source_of_vul = sqlalchemy.Column('source_of_vul', sqlalchemy.String(255), nullable=False, server_default='')
    vul_description = sqlalchemy.Column('vul_description', sqlalchemy.Text(), nullable=False)
    vul_announcement = sqlalchemy.Column("vul_announcement", sqlalchemy.Text(), nullable=False)
    reference_link = sqlalchemy.Column("reference_link", sqlalchemy.Text(), nullable=False)
    company = sqlalchemy.Column("company", sqlalchemy.String(255), nullable=False)
    detailUrl = sqlalchemy.Column("detailUrl", sqlalchemy.Text(), nullable=False)
