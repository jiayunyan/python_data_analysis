from pandas.io.parsers import read_csv
import numpy
import pandas
from numpy.random import seed
from numpy.random import rand
from numpy.random import random_integers
df=read_csv("F:/data/WHO.csv")
print("Dataframe",df)
print("Shape",df.shape)
print("Length",len(df))
print("Column Headers",df.columns)
print("Index",df.index)
print("Values",df.values)

country_col=df["Country"]
print("Type df",type(df))
print("Type country col",type(country_col))
print("Series shape",country_col.shape)
print("Series index",country_col.index)
print("Series values",country_col.values)
print("Series name",country_col.name)
print("Last 2 countries",country_col[-2:])
print("Last 2 countries type",type(country_col[-2:]))

last_col=df.columns[-1]
print("df signs\n",numpy.sign(df[last_col]))

df1=pandas.DataFrame({'Weather':['cold','hot','cold','hot'],'Food':['soup','soup','icecream','chocolate'],'Price':10*rand(4),'Number':random_integers(1,9,size=(4,))})
print(df1)
weather_group=df1.groupby('Weather')
i=0
for name,group in weather_group:
    i=i+1
    print("Group",i,name)
    print(group)

print("Weather group first\n",weather_group.first())
print("Weather group last\n",weather_group.last())
print("Weather group mean\n",weather_group.mean())

print(pandas.concat([df1[:2],df1[2:]]))
print(df1[:3].append(df1[2:]))

print(pandas.date_range('1/1/1990',periods=42,freq='D'))

print(pandas.pivot_table(df1,columns=['Food'],aggfunc=numpy.sum))




