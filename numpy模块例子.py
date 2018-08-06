# -*- coding: utf-8 -*-
import numpy
x=numpy.array(['a',8,'c',9])
print(x)
y=numpy.array([[2,6,7,9],[6,8,9,6],[8,7,5,1],[0,8,6,5]])
print(y)
print(x[2])
print(y[2][2])
x.sort()
y.sort()
print(x)
print(y)
print(y.max())

import pandas
a=pandas.Series([8,9,1,2])
print(a)
b=pandas.Series([8,9,1,2],index=["one","two","three","four"])
print(b)
c=pandas.DataFrame([[5,6,2,3],[8,4,6,3],[6,4,31,2]])
print(c)
d=pandas.DataFrame([[5,6,2,3],[8,4,6,3],[6,4,31,2]],columns=["one","two","three","four"])
print(d)
e=pandas.DataFrame({
    "one":4,"two":[6,2,3],"three":list(str(982))
})
print(e)
print(d.head())
print(d.tail(2))
print(d.describe())
print(d.T)


i=pandas.read_csv("F:/data/hexun.csv")
print(i.describe())
print(i.sort_values(by="21"))
j=pandas.read_excel("F:/data/abc.xls")
print(j)