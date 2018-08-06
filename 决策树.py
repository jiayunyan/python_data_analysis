import pandas
fname="F:/data/lesson.csv"
dataf=pandas.read_csv(fname,encoding="gbk")
print(dataf)
x=dataf.iloc[:,1:5].as_matrix()
y=dataf.iloc[:,5].as_matrix()
print(x)
print(y)
for i in range(0,len(x)):
    for j in range(0,len(x[i])):
        thisdata=x[i][j]
        if(thisdata=="是" or thisdata=="多" or thisdata=="高"):
            x[i][j]=int(1)
        else:
            x[i][j]=int(-1)
for i in range(0,len(y)):
    thisdata=y[i]
    if(thisdata=="高"):
        y[i]=1
    else:
        y[i]=-1
print(x)
print(y)

#转化格式，先转为数据框，仔转化为数组并指定格式
xf=pandas.DataFrame(x)
yf=pandas.DataFrame(y)
x2=xf.as_matrix().astype(int)
y2=yf.as_matrix().astype(int)
print(x2)
print(y2)
#建立决策树
from sklearn.tree import DecisionTreeClassifier as DTC
dtc=DTC(criterion="entropy")
dtc.fit(x2,y2)
#直接预测销量高低
import numpy
x3=numpy.array([[1,-1,-1,1],[1,1,1,1],[-1,1,-1,1]])
rst=dtc.predict(x3)
print(rst)
#可视化决策树
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
with open("F:/data/tree.dot","w") as file:
    file=export_graphviz(dtc,feature_names=["exercise","num","discount","book"],out_file=file)


