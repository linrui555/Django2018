import cx_Oracle as oracle
user="system"
passwd="Lr456852"
host="127.0.0.1"
port="1521"
sid="NIHAO"

dsn=oracle.makedsn(host, port, service_name=sid)
data=7782
# sql="INSERT INTO EMP VALUES(7888,'linrui','ANALYST',7566,to_date('2018-01-02','yyyy-mm-dd'),3000,NULL,20)"
sql=("update emp set ENAME='LINMIN' where empno=%d"%(data))
db=oracle.connect(user, passwd, dsn)
# def sqlSelect(sql,db):
#     cr=db.cursor()
#     cr.execute(sql)
#     rs=cr.fetchall()
#     cr.close()
#     return rs
#
# result=sqlSelect(sql,db)
# print(result)
def sqlDML(sql,db):
    cr=db.cursor()
    cr.execute(sql)
    db.commit()
    cr.close()

c=sqlDML(sql,db)
def sqlDML2(sql,data,db):
    cr = db.cursor()
    cr.execute(sql,data)
    db.commit()
    cr.close()
