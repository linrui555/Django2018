import cx_Oracle as oracle
import pymysql
user="system"
passwd="Lr456852"
host="127.0.0.1"
port="1521"
sid="NIHAO"


try:
    conn=pymysql.connect(host="192.168.174.139",port=3306,db='test2',user='root',passwd='root@123',charset='utf8')
    cs1=conn.cursor()
    cs1.execute('select * from bookinfo')
    rows=cs1.fetchall()
    print(rows)
    for row in rows:
        print(row[2])

    cs1.close()
    conn.close()


    dsn=oracle.makedsn(host, port, service_name=sid)
    # data=7782
    # sql="INSERT INTO EMP VALUES(7888,'linrui','ANALYST',7566,to_date('2018-01-02','yyyy-mm-dd'),3000,NULL,20)"
    db=oracle.connect(user, passwd, dsn)
    cr=db.cursor()
    sql = ('select * from emp where empno=7369')
    cr.execute(sql)
    rs=cr.fetchall()
    print(rs)
    g=cr.connection
    print(g)
    print("分段打印")
    for i in rs:
        print(i)


    cr.close()
    db.close()
except Exception as e:
        print(e)
# def sqlDML(sql,db):
#     cr=db.cursor()
#     cr.execute(sql)
#     db.commit()
#     cr.close()
#
# c=sqlDML(sql,db)
# def sqlDML2(sql,data,db):
#     cr = db.cursor()
#     cr.execute(sql,data)
#     db.commit()
#     cr.close()

   # def sqlSelect(sql,db):
   #      cr=db.cursor()
   #      cr.execute(sql)
   #      rs=cr.fetchall()
   #      cr.close()
   #      return rs
   #   result=sqlSelect(sql,db)
