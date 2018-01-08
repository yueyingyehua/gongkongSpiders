#coding:utf8

#Author: tsuki
#Date: 2017-12-09
#Time: 15:21
import sqlalchemy

from common.config.mysqlConfig import MysqlConfig


class UrlKeyWordEntity(MysqlConfig().getBaseModel()):
    __tablename__ = "urlKeyWord"
    __table_args__ = {
        "mysql_charset": "utf8"
    }

    id = sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True)
    #需要进行解析关键字的url
    url = sqlalchemy.Column('url', sqlalchemy.Text(), nullable=False)
    #url的标题
    urlTitle  = sqlalchemy.Column('urlTitle', sqlalchemy.Text())
    #搜索引擎
    searchEngine = sqlalchemy.Column('searchEngine', sqlalchemy.Text())
    #搜索的关键字
    searchWord = sqlalchemy.Column('searchWord', sqlalchemy.String(255), nullable=False, server_default= '')


