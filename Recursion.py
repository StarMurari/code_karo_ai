# Recursion in Python - Recursion is a programming technique where a function calls itself either directly or indirectly to solve a problem by breaking it into smaller, simpler subproblems.

# In Python, recursion is especially useful for problems that can be divided into identical smaller tasks, such as mathematical calculations, tree traversals or divide-and-conquer algorithms.

# Working of Recursion - A recursive function is just like any other Python function except that it calls itself in its body.

# def recursive_function(parameters):
#     if base_case_condition:
#         return base_result
#     else:
#         return recursive_function(modified_parameters)


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(8))

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else: 
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(6))

# break down full code 
# F(6) = F(5) + F(4)
# F(5) = F(4) + F(3)
# F(4) = F(3) + F(2)
# F(3) = F(2) + F(1)
# F(2) = F(1) + F(0)
# F(1) = 1
# F(0) = 0
# Calculate bottom-up:
# F(2) = 1 + 0 = 1
# F(3) = 1 + 1 = 2
# F(4) = 2 + 1 = 3
# F(5) = 3 + 2 = 5
# F(6) = 5 + 3 = 8


# Explanation :

# Base Cases: If n == 0, the function returns 0. If n == 1, the function returns 1. These two cases are necessary to stop the recursion.
# Recursive Case: function calls itself twice with decrements of n (i.e., fibonacci(n-1) and fibonacci(n-2)), summing results of these calls.


# Types of Recursion in Python : 
# Recursion can be broadly classified into two types: tail recursion and non-tail recursion. The main difference between them is related to what happens after recursive call.

# Tail Recursion: The recursive call is the last thing the function does, so nothing happens after it returns. Some languages can optimize this to work like a loop, saving memory.

# Non-Tail Recursion: The function does more work after the recursive call returns, so it can’t be optimized into a loop.


# Example of lambda function 

# name = "Hello Murari"
# printName = lambda val: val[0:8:1]

# print(printName(name))

# summul = lambda x, y: (x+y, x*y)
# calculate = summul(5,9)
# print(calculate)

# even = lambda x: True if(x%2 == 0) else False
# print(even(54))


# filter() Function in Python 
# filter() function in Python takes in a function and a list as arguments. This offers an elegant way to filter out all the elements of a sequence "sequence", for which the function returns True.
# n = [1, 2, 3, 4, 5, 6]
# even = filter(lambda x: x % 2 == 0, n)
# print(list(even))


# map() Function in Python - map() function in Python takes in a function and a list as an argument. The function is called with a lambda function and a new list is returned which contains all the lambda-modified items returned by that function for each item.
# a = [1,2,3,5,6]
# result = map(lambda x: x*2, a)
# print(list(result))


# reduce() Function in Python - reduce() function in Python takes in a function and a list as an argument. The function is called with a lambda function and an iterable and a new reduced result is returned. This performs a repetitive operation over the pairs of the iterable. The reduce() function belongs to the functools module. 
# from functools import reduce
a = [1, 2, 3, 4, 10]
b = reduce(lambda x, y: x * y, a)
print(b)