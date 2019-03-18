# 40. How to convert a numeric to a categorical (text) array?
# Q. Bin the petal length (3rd) column of iris_2d to form a text array, such that if petal length is:
# Less than 3 --> 'small'
# 3-5 --> 'medium'
# '>=5 --> 'large'
import	numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='float')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
small = iris[iris[:,2] < 3]
medium = iris[(iris[:,2] < 5) & (iris[:,2] >3)]
large = iris[iris[:,2] > 5]
print(small)
print(medium)
print( large)
# Bin petallength 
petal_length_bin = np.digitize(iris[:, 2].astype('float'), [0, 3, 5, 10])

# Map it to respective category
label_map = {1: 'small', 2: 'medium', 3: 'large', 4: np.nan}
petal_length_cat = [label_map[x] for x in petal_length_bin]

# View
petal_length_cat[:4]
#> ['small', 'small', 'small', 'small']