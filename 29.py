# 29. How to normalize an array so the values range exactly between 0 and 1?
# Q. Create a normalized form of iris's sepallength whose values range exactly between 0 and 1 so that the minimum has value 0 and maximum has value 1.

import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
normalize = (sepallength - sepallength.min())/ (sepallength.max() - sepallength.min())
print(normalize)