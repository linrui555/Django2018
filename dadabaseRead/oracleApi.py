#conding=utf-8
import cx_Oracle as oracle
class MysqlHelper(object):
    def __init__(self,host,port,user,passwd,sid,service_name):
        self.host=host
        self.port=port
        self.user=user
        self.passwd=passwd

        self.sid=sid
        self.service_name=service_name
    def open(self):
        self.dsn=oracle.makedsn(host=self.host,port=self.port,sid=self.sid,service_name=self.service_name)
        self.conn=oracle.connect(user=self.user,password=self.passwd,dsn=self.dsn)
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
