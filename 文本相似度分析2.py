from gensim import corpora,models,similarities
import jieba
from collections import defaultdict
doc1="F:/data/dmbj.txt"
doc2="F:/data/ljm.txt"
d1=open(doc1,'r', encoding='UTF-8').read()
d2=open(doc2,'r', encoding='UTF-8').read()
data1=jieba.cut(d1)
data2=jieba.cut(d2)
#"词语1 词语2 词语3 … 词语n"
data11=""
for item in data1:
    data11+=item+" "
data21=""
for item in data2:
    data21+=item+" "
documents=[data11,data21]
texts=[[word for word in document.split()]
       for document in documents]

frequency=defaultdict(int)
for text in texts:
    for token in text:
        frequency[token]+=1

texts=[[word for word in text if frequency[token]>5]
 for text in texts]

dictionary=corpora.Dictionary(texts)
dictionary.save("F:/data/wenben2.txt")
doc3="F:/data/gcd.txt"
d3=open(doc3,'r', encoding='UTF-8').read()
data3=jieba.cut(d3)
data31=""
for item in data3:
    data31+=item+" "
new_doc = data31
new_vec = dictionary.doc2bow(new_doc.split())
corpus=[dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize("F:/data/data3.mm",corpus)
tfidf=models.TfidfModel(corpus)
featureNum=len(dictionary.token2id.keys())
index=similarities.SparseMatrixSimilarity(tfidf[corpus],num_features=featureNum)
sim=index[tfidf[new_vec]]
print(sim)