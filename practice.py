# Write a program to ask the user to enter names of their three favourites movies & store them in a list 
# storemovies = []

# for i in range(3):
#     value = input(f"Enter {i+1} movie name: ")
#     storemovies.append(value)

# print(storemovies)

# Write a program to check if a list contains a palindrome of elements. [1, 2, 3, 2, 1], [1, 'abc', 'abc', 1]
# list1 = [1, 2, 3, 2, 1]

# list2 = list1.copy()

# if list1 == list2:
#     print("List1 contains a palindrome of elements")
# else:
#     print("List1 doesn't contains a palindrome of elements")


def is_palindrome(lst):
    return lst == lst[::-1]

list1 = [1, 2, 3, 2, 1]
list2 = [1, 'abc', 'abc', 1]
list3 = [1, 2, 3]

print(is_palindrome(list1))
print(is_palindrome(list2))
print(is_palindrome(list3))