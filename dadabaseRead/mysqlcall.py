#coding=utf-8
from dadabaseRead.mysqlApi import  MysqlHelper
try:
    name=input("请输入学生姓名")
    id=input("请输入学生编号")
    sql='update bookinfo set btitle=%s where id=%s'
    params=[name,id]
    sqlhelper=MysqlHelper("192.168.174.139",3306,'test2','root','root@123')
    sqlhelper.cud(sql,params)
except Exception as e:
    print(e)
