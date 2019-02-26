# 30. How to compute the softmax score?
# Q. Compute the softmax score of sepallength.
import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
softmax = (np.exp(sepallength)) / (np.sum(np.exp(sepallength)))
print(softmax)