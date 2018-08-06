#通过程序实现商品的聚类
import pandas as pda
import numpy as npy
import matplotlib.pylab as pyl
import pymysql
conn=pymysql.connect(host="127.0.0.1",user="root",passwd="yanjiayun0629",db="dangdang",charset='utf8')
sql="select price,comment from taob limit 300"
dataf=pda.read_sql(sql,conn)
x=dataf.iloc[:,:].as_matrix()
from sklearn.cluster import KMeans
kms=KMeans(n_clusters=3)
y=kms.fit_predict(x)
print(y)
#横坐标价格，纵坐标评论
for i in range(0,len(y)):
    if(y[i]==0):
        pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"*r")
    elif(y[i]==1):
        pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"sy")
    elif(y[i]==2):
        pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"*k")
pyl.xlabel("price")
pyl.ylabel("comment")
pyl.show()