from scipy import misc
import matplotlib.pyplot as plt
import numpy
face=misc.face()
acopy=face.copy()
aview=face.view()
plt.subplot(221)
plt.imshow(face)
plt.subplot(222)
plt.imshow(acopy)
plt.subplot(223)
plt.imshow(aview)
aview.flat=0
plt.subplot(224)
plt.imshow(aview)
plt.show()

face=misc.face()
xmax=face.shape[0]
ymax=face.shape[0]
face[range(xmax),range(ymax)]=0
face[range(xmax-1,-1,-1),range(ymax)]=0
plt.imshow(face)
plt.show()

face=misc.face()
xmax=face.shape[0]
ymax=face.shape[1]
def shuffle_indices(size):
    arr=numpy.arange(size)
    numpy.random.shuffle(arr)
    return arr

xindices=shuffle_indices(xmax)
numpy.testing.assert_equal(len(xindices),xmax)
yindices=shuffle_indices(ymax)
numpy.testing.assert_equal(len(yindices),ymax)
plt.imshow(face[numpy.ix_(xindices,yindices)])
plt.show()

ascent = misc.ascent()
#在对角线上画点
def get_indices(size):
    arr = numpy.arange(size)
    return arr %4==0
# 仅绘画出选定的点
ascent1 = ascent.copy()
xindices = get_indices(ascent.shape[0])
yindices = get_indices(ascent.shape[0])
#因为图片大小不是正方形，这里截取正方形图片
ascent1[xindices,yindices]=0
plt.subplot(211)
plt.imshow(ascent1)
ascent2 = ascent.copy()
#选取数组值介于最大值的1/4到3/4的元素，将其置0
ascent2[(ascent > ascent.max()/4) & (ascent <3 * ascent.max()/4)]=0
plt.subplot(212)
plt.imshow(ascent2)
#展示效果
plt.show()


