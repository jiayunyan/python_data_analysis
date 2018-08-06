import pandas
import matplotlib.pylab as pyl
data=pandas.read_csv("F:/data/hexun.csv",encoding='gbk')
print(data)
print(data.shape)
print(data.values[1])
print(data.values[1][1])
data2=data.T
y1=data2.values[3]
x1=data2.values[4]
# pyl.plot(x1,y1)
# pyl.show()
x2=data2.values[0]
pyl.plot(x2,y1)
pyl.show()