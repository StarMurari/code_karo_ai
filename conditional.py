# age = 17;
# if age > 18 : 
#     print("You are eligible for vote!")

# elif age < 18 :
#     print("You are not an adult")

# else : 
#     print("you are not eligible for vote!")


# Ternary Conditional Statement
# A ternary conditional statement is a compact way to write an if-else condition in a single line. It’s sometimes called a "conditional expression."
# age = 13
# s = "Adult" if age >= 18 else "Minor"
# print(s)



# Match-Case Statement
# match-case statement is Python's version of a switch-case found in other languages. It allows us to match a variable's value against a set of patterns.
number = 3

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")