import numpy
import pandas
import json
numpy.random.seed(42)
a=numpy.random.randn(3,4)
a[2][2]=numpy.nan
print(a)
numpy.savetxt("a1.csv",a,fmt='%.2f',delimiter=',',header="#1,#2,#3,#4")
df=pandas.DataFrame(a)
print(df)
df.to_csv('a2.csv',float_format='%.2f',na_rep="NAN!")


numpy.random.seed(42)
a=numpy.random.randn(365,4)
df=pandas.DataFrame(a)
df.to_excel('123.xlsx',sheet_name='Random Data')
print("Mean\n",pandas.read_excel('123.xlsx','Random Data').mean())


json_str='{"country":"USA","area_code":"0","ip":"128.0.0.1","country_code":"NL"}'
print(json_str)
data=json.loads(json_str)
print(data)
print("Country",data["country"])
data["country"]="UK"
print(json.dumps(data))

json_str='{"country":"USA","area_code":"0","ip":"128.0.0.1","country_code":"NL"}'
data=pandas.read_json(json_str,typ='series')
print("Series\n",data)
data["country"]="UK"
print("New Series\n",data.to_json())
print(data)





