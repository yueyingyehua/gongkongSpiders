#config:utf8
import sqlalchemy
import sqlalchemy.ext.declarative

class MysqlConfig():
        __mysqlPath = "mysql+pymysql://root:123456@localhost/gongkong?charset=utf8"
        __BaseModel = sqlalchemy.ext.declarative.declarative_base()
        __engine = sqlalchemy.create_engine(__mysqlPath, encoding = 'utf-8', echo = False)  #echo = True 则SQLAlchemy将会通过Python标准模块logging来输出日志

        def getEngine(self):
                return self.__engine

        def getBaseModel(self):
                return self.__BaseModel