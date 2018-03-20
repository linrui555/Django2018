from dadabaseRead.oracleApi import  MysqlHelper
try:
    name=input("请输入学生姓名")
    id=int(input("请输入学生编号"))
    sql=("""update EMP set ENAME= :name where EMPNO= :id""")
    params=[name,id]
    sqlhelper=MysqlHelper("127.0.0.1",1521,'system','Lr456852','NIHAO','NIHAO')
    sqlhelper.cud(sql,params)
except Exception as e:
    print(e)

