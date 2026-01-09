"""
np.delete(array, index, axis = None)
flatten array

"""


import numpy as np

arr = np.array([1,3,5,2,4,6])
# print(arr)

new_arr = np.delete(arr, 0)
# print(new_arr)

arr_2d = np.array([[1,2,3], [4,5,6]])
new_arr_2d = np.delete(arr_2d, 0, axis=0)

print(new_arr_2d)