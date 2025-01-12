# Functions allows us to use them in other files by importing them as modules to save time and space meaning we can create a function 
# once and use it multiple times in different files.

# We need to first define the function then we can call it anywhere on our files. 


"""
Call function to pass first parameter as text and second as the number of times it will print.
"""
# def print_message(text, number):
#     for ui in range(number):
#         print(text)

# print_message("Hello", 5)        

"""
Write a function that takes 2 numbers as parameters and returns the sum of those numbers.
"""

# def sum (a, b):
#     return a + b

# print(sum(18,12))

"""
Write a function that takes 2 numbers and returns the largest number.

"""

def largest(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return 0
    
num1 = int(input("Enter a number one: "))
num2 = int(input("Enter a number two: "))   

print(largest(num1, num2))