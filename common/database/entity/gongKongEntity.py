#config:utf8
import sqlalchemy

from common.config.mysqlConfig import MysqlConfig


class GongKongEntity(MysqlConfig().getBaseModel()):
    __tablename__ = "gongkong"
    __table_args__ = {
        "mysql_charset": "utf8"
    }

    id = sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True)
    productName = sqlalchemy.Column('productName', sqlalchemy.String(255), nullable = False, server_default =  '')
    keyWord = sqlalchemy.Column('keyWord', sqlalchemy.Text(), nullable = False, server_default = '')
    produceCategory = sqlalchemy.Column('produceCategory', sqlalchemy.Text(), nullable = False, server_default= '')
    brand = sqlalchemy.Column('brand', sqlalchemy.String(255), nullable = False, server_default = '')
    produceInfo = sqlalchemy.Column('produceInfo', sqlalchemy.Text(), nullable = False, server_default = '')
    detailsLinkUid = sqlalchemy.Column('detailsLinkUid', sqlalchemy.String(255), nullable = False, server_default= '')
