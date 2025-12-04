# Python Functions
# Python Functions are a block of statements that does a specific task. The idea is to put some commonly or repeatedly done task together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.

# Why use function - Code Reusability, Modularity, Redability, Maintainability 

# Defining a function 
# We can define a function in python using def keyword. A function might take input in the form of parameters.

# def fun():
#     print("Welcome to Python function world")

# fun()


# Function Arguments
# Arguments are the values passed inside the parenthesis of the function. A function can have any number of arguments separated by a comma.

# Syntax:

# def function_name(parameters):
#     """Docstring"""
#     # body of the function
#     return expression

# We will create a simple function in Python to check whether the number passed as an argument to the function is even or odd.

# def evenOdd(x):
#     if (x % 2 == 0):
#         return "Even"
#     else:
#         return "Odd"

# print(evenOdd(16))
# print(evenOdd(7))



# Types of Function Arguments
# Python supports various types of arguments that can be passed at the time of the function call.

# 1. Default Arguments - A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument.

# def myFun(x, y=50):
#     print("x: ", x)
#     print("y: ", y)

# myFun(10)


# 2. Keyword Arguments - values are passed by explicitly specifying the parameter names, so the order doesn’t matter.
# def student(fname, lname):
#     print(fname, lname)

# student(fname='Murari', lname='Pathak')
# student(lname='Pathak', fname='Murari')



# 3. Positional Arguments - In positional arguments, values are assigned to parameters based on their order in the function call.

# def printName(a, b, c): 
#     print(a, b, c)

# printName(2, 10, 15)



# 4. Arbitrary Arguments - In Python Arbitrary Keyword Arguments, *args and **kwargs can pass a variable number of arguments to a function using special symbols. There are two special symbols:

# *args in Python (Non-Keyword Arguments)
# **kwargs in Python (Keyword Arguments)
# This code separately shows non-keyword (*args) and keyword (**kwargs) arguments in the same function.

# def myFun(*args, **kwargs):
#     print("Non-Keyword Arguments (*args):")
#     for arg in args:
#         print(arg)

#     print("\nKeyword Arguments (**kwargs):")
#     for key, value in kwargs.items():
#         print(f"{key} == {value}")

# # Function call with both types of arguments
# myFun('Hey', 'Welcome', first='Murari', mid='kumar', last='Pathak')



# Function within Functions - A function defined inside another function is called an inner function (or nested function). It can access variables from the enclosing function’s scope and is often used to keep logic protected and organized.


# def murari():
#     a = "hello murari, how are you?"
#     def callMurari():
#         print(a)
    
#     callMurari()

# murari()



# Anonymous Functions - An anonymous function means that a function is without a name. As we already know the def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions.
# def cube(x): return x*x*x   # without lambda
# cube_l = lambda x : x*x*x  # with lambda

# print(cube(7))
# print(cube_l(7))