#coding:utf8

#Author: tsuki
#Date: 2017-12-08
#Time: 15:15
import sqlalchemy

from common.config.mysqlConfig import MysqlConfig
from common.log.MyLog import MyLog


class MysqlSQLAlchemyBaseDao():

    def __init__(self):
        self.DBSession = sqlalchemy.orm.sessionmaker(bind = MysqlConfig().getEngine())
        self.session = self.DBSession()
        MysqlConfig().getBaseModel().metadata.create_all(MysqlConfig().getEngine())
        self.logger = MyLog().getLogger()
