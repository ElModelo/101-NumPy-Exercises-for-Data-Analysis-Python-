# 15. How to make a python function that handles scalars to work on numpy arrays?
# Q. Convert the function maxx that works on two scalars, to work on two arrays.
import numpy as np
def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

maxx(1, 5)
#> 5