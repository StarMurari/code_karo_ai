"""
np.concatenate((array1, array2), axis=0)

axis = 0 -> vertical stacking
axis = 1 -> horizontal stacking

"""


import numpy as np

arr1 = np.array([1,3,5])
arr2 = np.array([2,4,6])

new_arr = np.concatenate((arr1, arr2))

print(new_arr)