#使用人工神经网络预测课程销量
#数据的读取与整理
import pandas as pda
fname="F:/data/lesson.csv"
dataf=pda.read_csv(fname,encoding="gbk")
x=dataf.iloc[:,1:5].as_matrix()
y=dataf.iloc[:,5].as_matrix()
for i in range(0,len(x)):
    for j in range(0,len(x[i])):
        thisdata=x[i][j]
        if(thisdata=="是" or thisdata=="多" or thisdata=="高"):
            x[i][j]=int(1)
        else:
            x[i][j]=0
for i in range(0,len(y)):
    thisdata=y[i]
    if(thisdata=="高"):
        y[i]=1
    else:
        y[i]=0
xf=pda.DataFrame(x)
yf=pda.DataFrame(y)
x2=xf.as_matrix().astype(int)
y2=yf.as_matrix().astype(int)

#使用人工神经网络模型
from keras.models import Sequential
from keras.layers.core import Dense,Activation
#建立模型
model=Sequential()
#输入层
model.add(Dense(10,input_dim=len(x2[0])))
model.add(Activation("relu"))
#输出层
model.add(Dense(1,input_dim=1))
model.add(Activation("sigmoid"))
#模型的编译
model.compile(loss="binary_crossentropy",optimizer="adam")
#训练
model.fit(x2,y2,nb_epoch=1000,batch_size=100)
#预测分类
rst=model.predict_classes(x).reshape(len(x))
print(rst)
x=0
for i in range(0,len(x2)):
    if(rst[i]!=y[i]):
        x+=1
print(1-x/len(x2))
import numpy as npy
x3=npy.array([[1,0,0,1],[1,1,1,1],[0,1,0,1],[1,0,0,0]])
rst=model.predict_classes(x3).reshape(len(x3))
print("其中第一门课的预测结果为:"+str(rst[0]))
print(rst)