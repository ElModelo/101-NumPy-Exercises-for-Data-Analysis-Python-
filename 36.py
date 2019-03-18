# 36. How to find the correlation between two columns of a numpy array?
# Q. Find the correlation between SepalLength(1st column) and PetalLength(3rd column) in iris_2d
import numpy as np
# Input
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
x = iris_2d[:,:1]
y = iris_2d[:,2:3]
mx = np.mean(x)
my = np.mean(y)
x_minus_mx = x - mx
y_minus_my = y - my
multiple = x_minus_mx * y_minus_my
sqt_x_minus_mx = x_minus_mx**2
sqt_y_minus_my = y_minus_my**2
sigma = np.sum(multiple)
sigmasqtx = np.sum(sqt_x_minus_mx)
sigmasqty = np.sum(sqt_y_minus_my)
r= sigma / (sigmasqtx * sigmasqty)**(1/2)
print(r)

