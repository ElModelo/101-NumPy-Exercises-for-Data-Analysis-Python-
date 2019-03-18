# 39. How to find the count of unique values in a numpy array?
# Q. Find the unique values and the count of unique values in iris's species
import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
species = iris[:,4]
unique = np.unique(species, return_counts = True)
print(unique)