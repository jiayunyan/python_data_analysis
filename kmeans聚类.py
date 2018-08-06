#kmeans算法
#通过程序实现录取学生的聚类
import pandas as pda
import numpy as npy
import matplotlib.pylab as pyl
fname="F:/data/luqu.xls"
dataf=pda.read_excel(fname)
x=dataf.iloc[:,1:4].as_matrix()
from sklearn.cluster import KMeans
kms=KMeans(n_clusters=2)
y=kms.fit_predict(x)
print(y)
#x代表学生序号，y代表学生类别
s=npy.arange(0,len(y))
pyl.plot(s,y,"o")
pyl.show()


