import numpy
import matplotlib.pylab as pyl
# data=numpy.random.random_integers(0,20,100)
# print(data)
# data1=numpy.random.normal(5.0,2.0,10)
# print(data1)
# data2=numpy.random.normal(10.0,1.0,1000)
# sty=numpy.arange(2,22,2)
# pyl.hist(data2,sty,histtype='stepfilled')
# pyl.show()
pyl.subplot(2,2,1)
x1=[1,2,3,4,5]
y1=[5,3,5,23,5]
pyl.plot(x1,y1)
pyl.subplot(2,2,2)
x2=[5,2,3,8,6]
y2=[7,9,12,12,3]
pyl.plot(x2,y2,'o')
pyl.subplot(2,1,2)
x3=[5,6,7,10,19,20,29]
y3=[6,2,4,21,5,1,5]
pyl.plot(x3,y3)
pyl.show()