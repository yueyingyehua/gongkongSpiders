#coding:utf8
import sqlalchemy

from common.config.mysqlConfig import MysqlConfig


class GongKongDCSEntity(MysqlConfig().getBaseModel()):
    __tablename__ = "gongkongDCS"
    __table_args__ = {
        "mysql_charset": "utf8"
    }

    id = sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True)
    categroy = sqlalchemy.Column('categroy', sqlalchemy.String(255), nullable=False, server_default= '')
    brand = sqlalchemy.Column('brand', sqlalchemy.String(255), nullable=False, server_default= '')
    product = sqlalchemy.Column('product', sqlalchemy.String(255), nullable=False, server_default= '')
    model = sqlalchemy.Column('model', sqlalchemy.String(255), nullable=False, server_default= '')
