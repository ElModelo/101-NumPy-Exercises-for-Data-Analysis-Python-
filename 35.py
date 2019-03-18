# 35. How to drop rows that contain a missing value from a numpy array?
# Q. Select the rows of iris_2d that does not have any nan value.
import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan
not_nan = iris_2d[~np.isnan(iris_2d)]
not_nan.resize(150,4)
print(not_nan)
