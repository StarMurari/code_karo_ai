# Loops in Python are used to repeat actions efficiently. The main types are For loops (counting through items) and While loops (based on conditions).

# For Loop
# For loops is used to iterate over a sequence such as a list, tuple, string or range. It allow to execute a block of code repeatedly, once for each item in the sequence.
# n = 4
# for i in range(0, n-1):
#     print(i)

# li = ["geeks", "for", "geeks"]
# for x in li:
#     print(x)
    
# tup = ("geeks", "for", "geeks")
# for x in tup:
#     print(x)
    
# s = "abc"
# for x in s:
#     print(x)
    
# d = dict({'x':123, 'y':354})
# for x in d:
#     print("%s  %d" % (x, d[x]))
    
# set1 = {10, 30, 20}
# for x in set1:
#     print(x)



# Iterating by Index of Sequences
# We can also use the index of elements in the sequence to iterate. The key idea is to first calculate the length of the list and then iterate over the sequence within the range of this length.
# li = ["Python", "Worlds", "Welcomes", "You"];
# for index in range(len(li)):
#     print(li[index])




# While Loop
# In Python, a while loop is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the line immediately after the loop in the program is executed.

# In below code, loop runs as long as the condition cnt < 3 is true. It increments the counter by 1 on each iteration and prints "Hello Geek" three times.
# cnt = 0;
# while (cnt < 5) : 
#     cnt = cnt + 1;
#     print("Hello Python Loop");

# print("program executed successfully!");



# Nested Loops
# Python programming language allows to use one loop inside another loop which is called nested loop. Following example illustrates the concept.
# from __future__ import print_function
# for i in range(1, 5):
#     for j in range(i):
#         print(i, end=' ')
#     print()




# Loop Control Statements
# Loop control statements change execution from their normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed. Python supports the following control statements. 

# Continue Statement
# The continue statement in Python returns the control to the beginning of the loop.
# for letter in 'helloPythonworldeee':
#     if letter == 'e' or letter == 's':
#         continue
#     print('Current Letter :', letter)

# Explanation: The continue statement is used to skip the current iteration of a loop and move to the next iteration. It is useful when we want to bypass certain conditions without terminating the loop.





# Break Statement
# The break statement in Python brings control out of the loop.
# for letter in 'helloPythonsworldeee':
#     if letter == 'e' or letter == 's':
#         break

# print('Current Letter :', letter)

# Explanation: break statement is used to exit the loop prematurely when a specified condition is met. In this example, the loop breaks when the letter is either 'e' or 's', stopping further iteration.





# Pass Statement
# We use pass statement in Python to write empty loops. Pass is also used for empty control statements, functions and classes.
for letter in 'helloPythonsworlds':
    pass
print('Last Letter :', letter)

# Explanation: In this example, the loop iterates over each letter in 'helloPythonsworldeee' but doesn't perform any operation, and after the loop finishes, the last letter ('s') is printed.