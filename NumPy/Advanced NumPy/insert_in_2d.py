import numpy as np

arr = np.array([[10,20], [40,50]])
print(arr)

new_arr = np.insert(arr, 1, [90,100], axis=None)
print(new_arr)