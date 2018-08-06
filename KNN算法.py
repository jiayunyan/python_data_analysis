from numpy import *
import operator
def knn(k,testdata,traindata,labels):
    traindatasize = traindata.shape[0]
    dif = tile(testdata, (traindatasize, 1)) - traindata
    sqdif = dif ** 2
    sumsqdif = sqdif.sum(axis=1)
    distance = sumsqdif ** 0.5
    sortdistance = distance.argsort()
    count = {}
    for i in range(0, k):
        vote = labels[sortdistance[i]]
        count[vote] = count.get(vote, 0) + 1
    sortcount = sorted(count.items(), key=operator.itemgetter(1), reverse=True)
    return sortcount[0][0]