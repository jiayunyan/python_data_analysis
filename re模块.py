# -*- coding: utf-8 -*-
import re
some_text='alpha,bata,,,,gama delta'
print (re.split('[,]+',some_text))
print (re.split('[,]+',some_text,maxsplit=2))
print (re.split('[,]+',some_text,maxsplit=1))
pat='[a-zA-Z]+'
text='"Hm...Err-- are you sure?" he said, sounding insecure'
print (re.findall(pat,text))
pat1=r'[.?\-",]+'
print (re.findall(pat1,text))
pat2='{name}'
text1='Dear {name},hello {name}'
xx=re.sub(pat2,'Jackson',text1)
print (xx)
print (re.escape('www.python.org'))
print (re.escape('But where is the ambiguity?'))

m=re.match(r'www\.(.*)\..{3}','www.python.org')
print (m.group(1))
print (m.start(1))
print (m.end(1))
print (m.span(1))

emphasis_pattern=r'\*([^\*]+)\*'
a=re.sub(emphasis_pattern,r'<em>\1</em>','hello,*world*!')
print (a)

import re
s='23432werwre2342werwrew'
p=r'(\d*)([a-zA-Z]*)'
m=re.match(p,s)
print (m.group())

import fileinput
pat=re.compile('From:(.*)<.*?>$')
for line in fileinput.input('kk'):
    m=pat.match(line)
    if m:print (m.group(1))



