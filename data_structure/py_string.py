# str = "Hello Python"

# str = '''Hello Murari,
# How are you?'''
# print(str[-(len(str)):-1])

# String Slicing - Slicing is a way to extract a portion of a string by specifying the start and end indexes. The syntax for slicing is string[start:end], where start starting index and end is stopping index (excluded).

# s = "Welcome to python world!"
# print(s[1:4])    # characters from index 1 to 3
# print(s[:3])     # from start to index 2
# print(s[3:])     # from index 3 to end
# print(s[::-1])   # reverse string



# String Iteration - Strings are iterable; you can loop through characters one by one.

# s = "Welcome to python world!"
# new_str = ""
# for i in s:
#     new_str += i
#     if(i == " "):
#         print(new_str)
#         new_str = ""



# String Immutability - Strings are immutable, which means that they cannot be changed after they are created. If we need to manipulate strings then we can use methods like concatenation, slicing or formatting to create new strings based on original.

# s = "Hello Murari"
# s = "M" + s[1:]   # create new string
# print(s)


# Deleting a String - In Python, it is not possible to delete individual characters from a string since strings are immutable. However, we can delete an entire string variable using the del keyword.

# Note: After deleting the string if we try to access s then it will result in a NameError because variable no longer exists.



# Updating a String - As strings are immutable, “updates” create new strings using slicing or methods such as replace().
# s = "hello learn"
# s1 = "H" + s[1:]                   # update first character
# s2 = s.replace("learn", "learn daily")  # replace word
# print(s)
# print(s1)
# print(s2)


# strip() removes leading and trailing whitespace from the string.
