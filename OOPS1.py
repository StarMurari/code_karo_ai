# Python OOP Concepts

# Object Oriented Programming is a fundamental concept in Python, empowering developers to build modular, maintainable and scalable applications.

# OOP is a way of organizing code that uses objects and classes to represent real-world entities and their behavior. In OOP, object has attributes thing that has specific data and can perform certain actions using methods.

# Key Features of OOP in Python:
# Organizes code into classes and objects
# Supports encapsulation to group data and methods together
# Enables inheritance for reusability and hierarchy
# Allows polymorphism for flexible method implementation
# Improves modularity, scalability, and maintainability


# 1. Class - A class is a collection of objects. Classes are blueprints for creating objects. A class defines a set of attributes and methods that the created objects (instances) can have.

# Some points on Python class:  

# Classes are created by keyword class.
# Attributes are the variables that belong to a class.
# Attributes are always public and can be accessed using the dot (.) operator. Example: Myclass.Myattribute


# Creating a Class -

# class Dog:
#     species = "Cannie"  # Class attribute

#     def __init__(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age  # Instance attribute




# 2. Objects - An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data.

# An object consists of:

# State: It is represented by the attributes and reflects the properties of an object.
# Behavior: It is represented by the methods of an object and reflects the response of an object to other objects.
# Identity: It gives a unique name to an object and enables one object to interact with other objects.

# Creating Object - Creating an object in Python involves instantiating a class to create a new instance of that class. This process is also referred to as object instantiation.

# class Dog:
#     species = "Canine"  # Class attribute

#     def __init__(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age  # Instance attribute

# # Creating an object of the Dog class
# dog1 = Dog("Buddy", 3)

# print(dog1.name) 
# print(dog1.species)



# Self Parameter - Self parameter is a reference to the current instance of the class. It allows us to access the attributes and methods of the object.

# Example: We create a Dog class with both class and instance attributes, then demonstrate how to access them using the self parameter.

# class Dog:
#     species = "Canine"  # Class attribute

#     def __init__(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age  # Instance attribute

# dog1 = Dog("Buddy", 3)  # Create an instance of Dog
# dog2 = Dog("Charlie", 5)  # Create another instance of Dog

# print(dog1.name, dog1.age, dog1.species)  # Access instance and class attributes
# print(dog2.name, dog2.age, dog2.species)  # Access instance and class attributes
# print(Dog.species)  # Access class attribute directly




# 3. Inheritance - Inheritance allows a class (child class) to acquire properties and methods of another class (parent class). It supports hierarchical classification and promotes code reuse.

# Types of Inheritance:
# Single Inheritance: A child class inherits from a single parent class.
# Multiple Inheritance: A child class inherits from more than one parent class.
# Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another class.
# Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
# Hybrid Inheritance: A combination of two or more types of inheritance.