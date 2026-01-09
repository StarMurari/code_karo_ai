import numpy as np 
import time as tm


# Multiplication in list
# lis1 = [1,2,3]
# print("print list", lis1*2)

# Numpy array
# np_array = np.array([1,2,5])
# print("print numpy array", np_array*2)


# Comparision between list an numpy array 
# start_time = tm.time()
# py_list = [i*2 for i in range(1000000)]
# print("my list is : ", py_list)
# print("Execution time of python list is", tm.time()-start_time)


# start_time = tm.time()
# np_array = np.arange(1000000) * 2
# print("Print NumPy array list ", np_array)
# print("Execution time of numpy array is", tm.time()-start_time)

# zeros = np.zeros((3,5))
# print("Zeros array \n", zeros)

# ones = np.ones((2,4))
# print("Ones array \n", ones)

# full_array = np.full((2,2), 7)
# print("Full Array \n", full_array)

# random_array = np.random.random((3,5))
# print("Print random array \n", random_array)

# sequence_array = np.arange(0, 11, 2) * 2
# print("Sequence array in numpy \n", sequence_array)



# Vector Matrix and Tensor
# vector = np.array([1,2,3])
# print("Vector", vector)

# matrix = np.array([[1,2,3], [4,5,6]])
# print("Matrix", matrix)

# tensor = np.array([[[1,2], [3,4]], [[8,9], [10,12]]])
# print("Tensor", tensor)


# arr = np.array([1,3,6,9,10])
# print(arr[0])
# arr[1] = 40
# print(arr)

# arr1 = np.array([[1,2,3], [2,3,4]])
# print(arr1.shape)
# print(arr1.dtype)

# arr2 = np.empty((2,4))
# print(arr2)

# arr3 = np.arange(0,5,2)
# print(arr3)


# Adding, removing, and sorting elements
# arr4 = np.array([2, 1, 5, 3, 7, 4, 6, 8])
# print(np.sort(arr4))

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = np.concatenate((a,b))
print("Arrays concatinated", c)