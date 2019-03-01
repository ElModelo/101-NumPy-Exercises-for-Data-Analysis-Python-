# 34. How to filter a numpy array based on two or more conditions?
# Q. Filter the rows of iris_2d that has petallength (3rd column) > 1.5 and sepallength (1st column) < 5.0
import numpy as np
# Input
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
filter_rows = iris_2d[(iris_2d[:,2]>1.5) & (iris_2d[:,0] <5)]
print(filter_rows)