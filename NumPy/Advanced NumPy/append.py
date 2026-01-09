"""
append() -> It append elements in the last indexes 
insert() -> It insert at specific position
"""


import numpy as np

arr = np.array([1,3,5])
new_arr = np.append(arr, [2,4,6])

print(new_arr)