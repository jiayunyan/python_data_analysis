f=open('1','w')
f.write('Hello,world!')
f.close()
f=open('1','r')
x=f.read(4)
print(x)
y=f.read()
print(y)
f.close()
def do_something(k):
    print(k.readlines())
with open('1') as kk:
    do_something(kk)

f = open(r'kk')
for i in range(3):
    print (str(i)+': '+f.readline())
f.close()

def process(string):
    print('Processing:',string)

import fileinput
for line in fileinput.input('kk'):
    process(line)

p=open('kk')
for lines in p:
    process(lines)
p.close()



alines=list(open('kk'))
print(alines)
first,second,third=open('kk')
print (first)
print(second)
print(third)

import sys
for aline in sys.stdin:
    process(aline)