# 28. How to compute the mean, median, standard deviation of a numpy array?
# Q. Find the mean, median, standard deviation of iris's sepallength (1st column)
import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='float', usecols = 0)
mean = np.mean(iris)
median = np.median(iris)
standard_deviation = np.std(iris)
print("the mean of iris's sepallength is: " + str(mean))
print("the median of iris's sepallength is: " + str(median))
print("the standard deviation of iris's sepallength is: " + str(standard_deviation))