# -*- coding: utf-8 -*-
import matplotlib.pylab as pyl
import matplotlib.pyplot as plt
import numpy
# x=[1,3,5,8]
# y=[3,7,8,4]
# x1=[4,7,9,10]
# y1=[6,8,3,9]
# pyl.plot(x,y,"r-")
# pyl.plot(x,y,'*')
# pyl.plot(x1,y1,"b")
# pyl.title("图")
# pyl.xlabel("age")
# pyl.ylabel("people")
# pyl.xlim(0,10)
# pyl.ylim(0,10)
# pyl.show()
x=[1,2,3,4,5,6,7,8,9]
y=[2,12,22,33,44,55,66,75,85]
plt.scatter(x,y,s=400*y,c='b',alpha=0.5)
plt.show()