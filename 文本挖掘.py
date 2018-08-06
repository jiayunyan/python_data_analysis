import jieba
sentence="我爱上海东方明珠"
w1=jieba.cut(sentence,cut_all=True)
for item in w1:
    print(item)
print("")
w2=jieba.cut(sentence,cut_all=False)
for item in w2:
    print(item)
print("")
w3=jieba.cut_for_search(sentence)
for item in w3:
    print(item)
print("")

import jieba.posseg
w4=jieba.posseg.cut(sentence)
for item in w4:
    print(item.word+"----"+item.flag)

import jieba.analyse
tag=jieba.analyse.extract_tags(sentence,3)
print(tag)

w5=jieba.tokenize(sentence)
for item in w5:
    print(item)