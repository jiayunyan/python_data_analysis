import pandas
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR
fname="F:/data/luqu.xls"
dataframe=pandas.read_excel(fname,index_col=None)
print(dataframe)
x=dataframe.iloc[:,1:4].as_matrix()
print(x)
y=dataframe.iloc[:,0:1].as_matrix()
print(y)
dataf=dataframe.iloc[:,1:4]
print(dataf)
r1=RLR()
r1.fit(x,y)
r1.get_support()#特征筛选
print(dataf.columns[r1.get_support()])
t=dataf[dataf.columns[r1.get_support()]].as_matrix()
print(t)
r2=LR()
r2.fit(t,y)
print("训练结束")
print("模型正确率为:"+str(r2.score(x,y)))