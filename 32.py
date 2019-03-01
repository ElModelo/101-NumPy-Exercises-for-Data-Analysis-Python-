# 32. How to insert values at random positions in an array?
# Q. Insert np.nan values at 20 random positions in iris_2d dataset
import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='object')
i = np.random.randint(len(iris_2d), size = 20)
j = np.random.randint(4,size=20)
iris_2d[i,j] = np.nan
print(iris_2d)