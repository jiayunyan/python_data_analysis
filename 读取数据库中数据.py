import pymysql
import pandas
conn = pymysql.connect(host="127.0.0.1", user="root", passwd="yanjiayun0629",db="dangdang",charset='utf8')
sql="select * from goods"
k=pandas.read_sql(sql,conn)
print(k)

l=pandas.read_html("F:/data/abc.html")
print(l)
m=pandas.read_html("https://book.douban.com/")
print(m)
n=pandas.read_table("F:/data/abc.txt")
print(n)