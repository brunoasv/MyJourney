#Conditionals if statements

# != different
"""
This program is able to catch an error: Error Handling-(try-except block) when the user enter a value that is not a int, 
in other words, a string.
"""
# user_age = input("Enter your age: ")

# try:
#     age = int(user_age)

#     if age >= 21:
#         print("You may enter the club and have drinks")
#     else:
#         if age >= 18:
#             print ("You can enter the club but not have drinks")
#         else:
#             print("You need to be at least 18 years old.")

# except ValueError:
#     print("Enter a number.")

"""
Get 3 numbers from user and compare it whether they are equal or not
"""

# n1 = int(input("Enter number one: "))
# n2 = int(input("Enter number two: "))
# n3 = int(input("Enter number three: "))

# if n1 == n2 and n1 == n3:
#     print("n1 is equal to n2 and n3")
# else:
#     print("They are not equal")


"""
Control flow structure: match case.
Example:
Option 1: Add 10
Option 2: Multiple 10
Option 3: Divide by 2
Print total.
"""

amount = int(input("Enter a number: "))
n = int(input("Select an option from 1 to 3: "))
match n:
    case 1:
        amount = amount + 10
    case 2:
        amount = amount * 10
    case 3:
        amount = amount / 2
    case other:
        print("Try next time")

print(amount)
