"""
.ravel() -> return view
.flatten() -> return copy but doesn't affect the original array
"""

import numpy as np

arr_2d = np.array([[1,2,3], [4,5,6]])

print(arr_2d.ravel())
print(arr_2d.flatten())