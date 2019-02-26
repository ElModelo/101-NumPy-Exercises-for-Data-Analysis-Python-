# 31. How to find the percentile scores of a numpy array?
# Q. Find the 5th and 95th percentile of iris's sepallength
import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
five = np.percentile(sepallength, 5)
ninety_five = np.percentile(sepallength, 95)
print(five, ninety_five)
