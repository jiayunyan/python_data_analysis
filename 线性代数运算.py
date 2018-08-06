import numpy
import pandas
data=pandas.read_csv("F:/data/hexun.csv",encoding='gbk',usecols=(3,))
print(data)
print(data.max())
print(numpy.max(data))
print(data.min())
print(numpy.min(data))
print(data.mean())
print(numpy.mean(data))
print(data.std())
print(numpy.std(data))
print(data.median())
print(numpy.median(data))

A=numpy.mat("2 4 6;4 2 6;10 -4 18")
print("A\n",A)
inverse=numpy.linalg.inv(A)
print("inverse\n",inverse)
print(A*inverse)
print(A*inverse-numpy.eye(3))

A=numpy.mat("1 -2 1;0 2 -8;-4 5 9")
print("A\n",A)
b=numpy.array([0,8,-9])
print("b\n",b)
x=numpy.linalg.solve(A,b)
print("Solution",x)
print("Check\n",numpy.dot(A,x))

A=numpy.mat("3 -2;1 0")
print("A\n",A)
print("Eigenvalues",numpy.linalg.eigvals(A))
eigenvalues,eigenvectors=numpy.linalg.eig(A)
print("First tuple of eig",eigenvalues)
print("Second tuple of eig",eigenvectors)
for i in range(len(eigenvalues)):
    print("Left",numpy.dot(A,eigenvectors[:,i]))
    print("Right",eigenvalues[i]*eigenvectors[:,i])



