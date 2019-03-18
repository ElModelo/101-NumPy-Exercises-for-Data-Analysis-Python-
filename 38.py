# 38. How to replace all missing values with 0 in a numpy array?
# Q. Replace all ccurrences of nan with 0 in numpy array
import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan
iris_2d[np.isnan(iris_2d)] = 0
print(iris_2d)