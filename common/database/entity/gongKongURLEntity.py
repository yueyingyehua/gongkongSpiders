#coding:utf8
import sqlalchemy

from common.config.mysqlConfig import MysqlConfig


class GongKongURLEntity(MysqlConfig().getBaseModel()):
    __tablename__ = "gongkongURL"
    __table_args__ = {
        "mysql_charset": "utf8"
    }

    id = sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True)
    detailsLink = sqlalchemy.Column('detailsLink', sqlalchemy.String(255), unique= True, nullable= False, server_default= '')
    uuid = sqlalchemy.Column('uuid', sqlalchemy.String(255), nullable= False, server_default= '')
