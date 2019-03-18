# 37. How to find if a given array has any null values?
# Q. Find out if iris_2d has any missing values.
import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
any_nan = np.any(np.isnan(iris_2d))
print(any_nan)