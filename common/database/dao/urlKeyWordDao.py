#coding:utf8

#Author: tsuki
#Date: 2017-12-09
#Time: 15:20
from common.database.dao.mysqlSQLAlchemyBaseDao import MysqlSQLAlchemyBaseDao
from common.database.entity.urlKeyWordEntity import UrlKeyWordEntity


class UrlKeyWordDao(MysqlSQLAlchemyBaseDao):

    def insert(self, datas):
        try:
            for data in datas:
                urlEntity = UrlKeyWordEntity(url=data['url'],
                                             urlTitle=data['urlTitle'],
                                             searchEngine=data['searchEngine'],
                                             searchWord=data['searchWord'])
                self.session.add(urlEntity)
            self.session.commit()
        except Exception as excep:
            self.logger.error("insert error {}".format(excep))
            self.session.rollback()
            raise
        self.session.close()

    def listURL(self):
        return self.session.query(UrlKeyWordEntity).all()

    def listURLByEngine(self, engine):
        return self.session.query(UrlKeyWordEntity).filter_by(searchEngine = engine).all()

    def listURLBySearchWord(self, searchWord):
        return self.session.query(UrlKeyWordEntity).filter_by(searchWord = searchWord).all()






