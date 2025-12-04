# print anything in python

# print("I have no Indentation ");
# print("I have tab Indentation ");

# take single input from user
# name = input("Enter your name: ")
# print("Hello,", name, "! Welcome!")

#Take Multiple Input in Python
# name, age = input("Enter your name and age: ").split();
# print("Hello,", name, "! You are", age, "years old");

# x, y, z = input("Enter three numbers: ").split();
# print("The sum of three numbers is:", int(x) + int(y) + int(z));

# print a variable in python
# murari = "Murari is a funny developer";
# age = 25;
# print(murari, "he is", age, "years old");


# By default input is taken as string
# Change the Type of Input in Python
# x = int(input("Enter a number: "));
# y = int(input("Enter another number: "));
# print("The sum of two numbers is: ", x+y);

# Print Float or Decimal Number in Python
# x = float(input("Enter a decimal number: "));
# print("The decimal number is: ", x);

# Find DataType of Input in Python
# a = "Hello World"
# b = 10
# c = 11.22
# d = ("Murari", "works", "in", "Aeri")
# e = ["Murari", "is", "Murari"]
# f = {"Murari": 6, "kumar":5, "Pathak":6}

# print(type(a), type(b), type(c), type(d), type(e), type(f));


# In Python, variables are used to store data that can be referenced and manipulated during program execution. 
# A variable is essentially a name that is assigned to a value.

# Unlike Java and many other languages, Python variables do not require explicit declaration of type.
#The type of the variable is inferred based on the value assigned.
# x = 5
# name = "Samantha"  
# print(x)
# print(name)

# Rules for Naming Variables
# To use variables effectively, we must follow Python’s naming rules:

# Variable names can only contain letters, digits and underscores (_).
# A variable name cannot start with a digit.
# Variable names are case-sensitive like myVar and myvar are different.
# Avoid using Python keywords like if, else, for as variable names.

# Value keywords in Python - None, True, False, 
# operators keyword are - and, or, not, is, in, 
# Control flow keywords are - if, else, elif, for, while, break, continue, pass, try, except, finally, raise, assert
# Function and Class - def, return, lambda, yield, class
# Context Managments - with, as
# Import and Module - import, from
# Scope and Namespace - global, nonlocal
# Async Programming - async, await,

# Valid Examples of Variables in Python
# age = 21
# _colour = "lilac"
# total_score = 90

# Invalid Examples of Variables in Python
# 1age = 21
# age@ = 21
# class = "Sum"

# Variables in Python are assigned values using the
# x = 5 

# Python variables are dynamically typed, meaning the same variable can hold different types of values during execution.
# x = 10
# x = "Now a string"

# Python allows assigning the same value to multiple variables in a single line, which can be useful for initializing variables with the same value.
# a = b = c = 100
# print(a, b, c)


# Type Casting a Variable
# Type casting refers to the process of converting the value of one data type into another. 
# Python provides several built-in functions to facilitate casting, including int(), float() and str() among others.

# x = "10";
# print(int(x));

# Object Reference in Python
# Let us assign a variable x to value 5.
# x = 5
# When x = 5 is executed, Python creates an object to represent the value 5 and makes x reference this object.
# Now, let's assign another variable y to the variable x.
# y = x
# Python encounters the first statement, it creates an object for the value 5 and makes x reference it. The second statement creates y and references the same object as x, not x itself. This is called a Shared Reference, where multiple variables reference the same object.
# Now, if we write
# x = 'Geeks'
# Python creates a new object for the value "Geeks" and makes x reference this new object.
# The variable y remains unchanged, still referencing the original object 5.
# If we now assign a new value to y:
# y = "Computer"
# Python creates yet another object for "Computer" and updates y to reference it.
# The original object 5 no longer has any references and becomes eligible for garbage collection.
# Python variables hold references to objects, not the actual objects themselves.
# Reassigning a variable does not affect other variables referencing the same object unless explicitly updated.


# Delete a Variable Using del Keyword
# We can remove a variable from the namespace using the del keyword. This deletes the variable and frees up the memory it was using.

# x = 10
# print(x)
# del x

# x = "Hello Murari";
# print(len(x));

# a, b = 1, 3;
# a, b = b, a;
# print(a, b);



# Python Operators - Operators in general are used to perform operations on values and variables.
# Operators: Special symbols like -, + , * , /, etc.
# Operands: Value on which the operator is applied.

# Python Arithmetic operators are used to perform basic mathematical operations like addition, subtraction, multiplication and division.
# Variables
# a = 15
# b = 4

# Addition
# print("Addition:", a + b)  

# Subtraction
# print("Subtraction:", a - b) 

# Multiplication
# print("Multiplication:", a * b)  

# Division
# print("Division:", a / b) 

# Floor Division
# print("Floor Division:", a // b)  

# Modulus
# print("Modulus:", a % b) 

# Exponentiation
# print("Exponentiation:", a ** b)

# Comparison Operators - Comparison operators are used to compare values.
# It returns either True or False according to the condition.
# a = 13
# b = 33

# print(a > b)
# print(a < b)
# print(a == b)
# print(a != b)
# print(a >= b)
# print(a <= b)

# Logical Operators - perform Logical AND, Logical OR and Logical NOT operations. It is used to combine conditional statements.
# The precedence of Logical Operators in Python is as follows:
    # Logical not
    # logical and
    # logical or

# a = True
# b = False
# print(a and b)
# print(a or b)
# print(not a)


# Bitwise Operators - act on bits and perform bit-by-bit operations. These are used to operate on binary numbers.

# Bitwise Operators in Python are as follows:
    # Bitwise NOT
    # Bitwise Shift
    # Bitwise AND
    # Bitwise XOR
    # Bitwise OR

# a = 10
# b = 4

# print(a & b) - 0
# print(a | b) - 14 
# print(~a) - -11
# print(a ^ b) - 14 
# print(a >> 2) - 2
# print(a << 2) - 40


# Assignment Operators - Used to assign values to the variables. This operator is used to assign the value of the right side of the expression to the left side operand.

# a = 10
# b = a
# print(b)
# b += a
# print(b)
# b -= a
# print(b)
# b *= a
# print(b)
# b <<= a
# print(b)


# Identity Operators
# In Python, is and is not are the identity operators both are used to check if two values are located on the same part of the memory. Two variables that are equal do not imply that they are identical. 

# is          True if the operands are identical 
# is not      True if the operands are not identical

# a = 10
# b = 20
# c = a
# print(a is not b)
# print(a is c) 


# Membership Operators 
# In Python, in and not in are the membership operators that are used to test whether a value or variable is in a sequence.

# in            True if value is found in the sequence
# not in        True if value is not found in the sequence

# x = 24
# y = 20
# list = [10, 20, 30, 40, 50]

# if (x not in list):
#     print("x is NOT present in given list")
# else:
#     print("x is present in given list")

# if (y in list):
#     print("y is present in given list")
# else:
#     print("y is NOT present in given list")


# Ternary Operator - Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false. 
# It simply allows testing a condition in a single line replacing the multiline if-else, making the code compact.

# Syntax :  [on_true] if [expression] else [on_false] 

# a, b = 10, 20
# min = a if a < b else b

# print(min)








# Python Keywords - Keywords in Python are special reserved words that are part of the language itself. They define the rules and structure of Python programs which means you cannot use them as names for your variables, functions, classes or any other identifiers.

import keyword

# printing all keywords at once using "kwlist()"
print("The list of keywords are : ")
print(keyword.kwlist)