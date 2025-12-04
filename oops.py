# Class - Class is a blueprint for creating objects. 
# creating class 
# class Student:
    # name = "Murari Pathak"


# creating object (instance)
# s1 = Student()
# print(s1.name)

# Example of Class 
# class Car:
#     color = "yellow"
#     brand = "Mercedes"

# car1 = Car()
# print(car1.color)
# print(car1.brand)


# Constructor - All classes have a function called __init__(), which is always executed when the object is being initiated.
class Student:

    # Class Attribute
    college_name = "Sir M. Visvesvaraya Institute of Technology"  # access using Class.attribute_name (Student.college_name)
    name = "Murari Pathak"
    # Default Constructor
    def __init__(self):
        print("Print anything")

    # Parameterized constructor
    def __init__(self, name):
        self.name = name  # object.attribute > class.attribute (object attribute precedence is always greater than class attribute)
        print("Adding new data in the database...")

# s1 = Student("Murari Kumar")
# print(s1.name)

# s2 = Student("Mithilesh Kumar")
# print(s2.name)

# Print Class attribute
# print(Student.college_name)

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class 
# Constructor call for each object


# Class & instance Attributes
# class.attribute_name
# object.attribute_name


# Methods - Methods are functions that belong to objects.

class Student:
    def __init__(self, name):
        self.name = name
    
    def hello(self):
        print("hello", self.name)
    

s1 = Student("Murari")
s1.hello()