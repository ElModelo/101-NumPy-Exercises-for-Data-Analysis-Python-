# 41. How to create a new column from existing columns of a numpy array?
# Q. Create a new column for volume in iris_2d, where volume is (pi x petallength x sepal_length^2)/3
import numpy as np
# Input
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
x = (np.pi)*(iris_2d[:,2].astype('float'))*((iris_2d[:,1].astype('float'))** 2) 
y = np.append(iris_2d, x[:, np.newaxis], axis = 1)
print(y)