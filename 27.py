# 27. How to convert a 1d array of tuples to a 2d numpy array?
# Q. Convert the 1D iris to 2D array iris_2d by omitting the species text field.
import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_1d = np.genfromtxt(url, delimiter=',', dtype=None, usecols = (0,1,2,3))
print(iris_1d)