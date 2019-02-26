# 26. How to extract a particular column from 1D array of tuples?
# Q. Extract the text column species from the 1D iris imported in previous question.
import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_1d = np.genfromtxt(url, delimiter=',', dtype=object, usecols = (4))
print(iris_1d[:3])