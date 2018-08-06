import numpy
a=numpy.array([[1,2,3],[4,5,6]])
b=numpy.array([[7,8,9],[10,11,12]])
c=numpy.concatenate((a,b))
print(c)

import pymysql
import pandas
conn = pymysql.connect(host="localhost", user="root", passwd="yanjiayun0629",db="dangdang",charset='utf8')
sql="select price,comment from taob"
data=pandas.read_sql(sql,conn)
print(data)
#离差标准化
data2=(data-data.min())/(data.max()-data.min())
print(data2)
#标准差标准化
data3=(data-data.mean())/data.std()
print(data3)
#小数定标规范化
data4=data/10**(numpy.ceil(numpy.log10(data.abs().max())))
print(data4)
data5=data[u"price"].copy()
data6=data5.T
data7=data6.values
k=3
c1=pandas.cut(data7,k,labels=["便宜","适中","贵"])
print(c1)
k=[0,50,100,300,500,2000,data7.max()]
c2=pandas.cut(data7,k,labels=["非常便宜","便宜","适中","有点贵","很贵","非常贵"])
print(c2)


conn=pymysql.connect(host="127.0.0.1",user="root",passwd="yanjiayun0629",db="dangdang",charset='utf8')
sql="select * from myhexun"
data8=pandas.read_sql(sql,conn)
print(data8)
ch=data8[u"comment"]/data8["hits"]
data8[u"评点比"]=ch
file="F:/data/hexun.xls"
data8.to_excel(file,index=False)