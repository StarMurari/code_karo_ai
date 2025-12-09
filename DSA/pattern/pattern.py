# First Program
import time 
start = time.time()
# for i  in range(1,5):
#     for j in range(1, 5):
#         print(j, end=" ")
#     print()

# i = 1
# while i < 5:
#     j = 1
#     while j < 5:
#         print(4-j+1, end=" ")
#         j = j + 1
#     i = i+1
#     print()

# Second Program 
# 123
# 456
# 789

# i=1
# num = 1
# while i < 4:
#     j = 1
#     while j < 4:
#         print(num, end=" ")
#         j = j + 1
#         num = num + 1
#     i = i + 1
#     print()

# Program Third 
# *
# **
# ***
# ****
# *****

# i = 1
# while i < 6:
#     j = 1
#     while j < i + 1:
#         print("*", end=" ")
#         j = j + 1
#     i = i + 1
#     print()


# i = 1
# while i < 5:
#     j = 1
#     while j < i + 1:
#         print(i, end=" ")
#         j = j + 1
#     i = i + 1
#     print()

# 1
# 23
# 345
# 4567
# 56789

# Approach with extra variable 
# i = 1
# while i < 5:
#     j = 1
#     row = i
#     while j < i + 1:
#         print(row, end=" ")
#         j = j + 1
#         row = row + 1
#     print()
#     i = i + 1

# Approach without extra variable 
# i = 1
# while i < 5:
#     j = 1
#     while j < i + 1:
#         print(j-1+i, end=" ")
#         j = j + 1
#     print()
#     i = i + 1


# i = 1
# while i < 5:
#     j = 1
#     while j < i + 1:
#         print(i-j+1, end=" ")
#         j = j + 1
#     print()
#     i = i + 1


# i = 1
# while i < 4:
#     j = 1
#     while j < 4:
#         print(chr(ord("A")+i-1), end=" ")
#         j = j + 1
#     print()
#     i = i + 1


# i = 1
# while i < 4:
#     j = 1
#     while j < 4:
#         print(chr(ord("A")+j-1), end=" ")
#         j = j + 1
#     print()
#     i = i + 1


# i = 1
# count = 0
# while i < 4:
#     j = 1
#     while j < 4:
#         print(chr(ord("A")+count), end=" ")
#         count = count + 1
#         j = j + 1
#     print()
#     i = i + 1


# i = 1
# while i < 4:
#     j = 1
#     while j < 4:
#         print(chr(ord("A") + i + j - 2), end=" ")
#         j = j + 1
#     print()
#     i = i + 1


# i = 1
# while i < 4:
#     j = 1
#     while j < i + 1:
#         print(chr(ord('A') + i - 1 ), end=" ")
#         j = j + 1
#     i = i + 1
#     print()
 

# i = 1
# while i <= 4:
#     j = 1
#     start = ord('A') + 4 - i
#     while j <= i:
#         print(chr(start), end=" ")
#         j = j + 1
#         start = start + 1
#     i = i + 1
#     print()

# 000*
# 00**
# 0***
# ****

# i = 1
# while i <= 4:
#     space = 4 - i
#     while space:
#         print(" ", end=" ")
#         space = space - 1
    
#     j = 1
#     while j <= i:
#         print("*", end=" ")
#         j = j + 1
#     i = i + 1
#     print()
  

# i = 1
# while i <= 5:
#     star = 5 - i + 1
#     while star:
#         print("*", end=" ")
#         star = star - 1
    
#     j = 1
#     while ( j <= i): 
#         print(" ", end=" ")
#         j = j + 1
#     i = i + 1
#     print()


# i = 5
# while i > 0:
#     j = 1
#     while j <= i:
#         print("*", end=" ")
#         j = j + 1
#     i = i - 1
#     print()


# i = 1
# while i <= 4:
#     space = i - 1
#     while space:
#         print(" ", end=" ")
#         space = space - 1
    
#     j = 1
#     while j <= 4 - i + 1:
#         print(i, end=" ")
#         j = j + 1
#     i = i + 1
#     print()


#   *
#  ***
# *****

# i = 1
# while i <= 4:
#     space = 4 - i
#     while space:
#         print(" ", end=" ")
#         space = space - 1
#     j = 1
#     while j <= i:
#         print("*", end=" ")
#         j = j + 1

#     y = 1
#     while y <= i - 1:
#         print("*", end=" ")
#         y = y + 1
#     i = i + 1
#     print()


# i = 1
# while i <= 5:
#     space = 5 - i
#     while space:
#         print(" ", end=" ")
#         space = space - 1
    
#     j = 1
#     while j <= i:
#         print(j, end=" ")
#         j = j + 1


#     x = 1
#     while x <= i - 1:
#         print(i-x, end=" ")
#         x = x + 1
#     i = i + 1
#     print()



# 12344321
# 123**321
# 12****21
# 1******1

i = 1
while i <= 4:
    j = 1
    while j <= 4 - i + 1:
        print(j, end=" ")
        j = j + 1
    star = i - 1
    while star:
        print("*", end=" ")
        star = star - 1
    sstar = 1
    while sstar <= i - 1:
        print("*", end=" ")
        sstar = sstar + 1
    x = 4 - i + 1
    while x:
        print(x, end=" ")
        x = x - 1
    i = i + 1
    print()


end = time.time()
print("\nExecution time:", end - start, "seconds")