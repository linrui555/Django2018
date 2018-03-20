#conding=utf-8
import pymysql
class MysqlHelper(object):
    def __init__(self,host,port,db,user,passwd,charset="utf8"):
        self.host=host
        self.port=port
        self.db=db
        self.user=user
        self.passwd=passwd
        self.charset=charset
    def open(self):
        self.conn=pymysql.connect(host=self.host,port=self.port,db=self.db,user=self.user,passwd=self.passwd,charset=self.charset)
        self.cursor=self.conn.cursor()
    def close(self):
        self.cursor.close()
        self.conn.close()
    def cud(self,sql,params):
        try:
            self.open()
            self.cursor.execute(sql,params)
            self.conn.commit()
            self.close()
        except Exception as e:
            print(e)
    def all(self,sql,pramas):
        try:
            self.open()
            self.cursor.execute(sql,pramas)
            result=self.cursor.fetchall()
            self.close()
            return result
        except Exception as e:
            print(e)
