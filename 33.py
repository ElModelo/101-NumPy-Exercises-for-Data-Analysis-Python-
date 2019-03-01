# 33. How to find the position of missing values in numpy array?
# Q. Find the number and position of missing values in iris_2d's sepallength (1st column)
import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float')
iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan
is_nan = np.isnan(iris_2d[:,0])
number_of_nan = is_nan.sum()
print(number_of_nan)
where_is_nan = np.where(is_nan)
print(where_is_nan)
