# What is a list in Python - A list in Python is a built-in data structure used to store an ordered collection of items in a single variable.

# arr = [1,2,3,4,5]

# print(arr[len(arr)-3:len(arr)]) # Get last three elements of a list
# print(arr[0:5:2]) # skip elements of a list

# print(arr[2:1])  #If start > end, there is no valid forward range, so Python returns an empty list instead of throwing an error.

# If you explicitly provide a negative step, slicing behaves differently.
# print(arr[4:1:-1])  # Output will be [5, 4, 3]



#NESTED LISTS (Important for NumPy)
lst = [[1,2,3],[4,5,6],[7,8,9]]

# Access an element from 2D list
# print(lst[0][1])
# print(len(lst))

# Iterate over 2D list
# for row in lst:
#     for element in row:
#         print(element, end=",")
#     print()

# Using index based loops
# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         print(lst[i][j])


# Using enumerate() (Clean & Professional)
# for i, row in enumerate(lst):
#     for j, value in enumerate(row):
#         print(f"lst[{i}][{j}] =", value)


# Using List Comprehension (Flattening)
flat = [item for row in lst for item in row]
print(flat)