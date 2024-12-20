"""
For loop --> when you know the number of iterations you want to have

While loop ----> when you it goes indefinately.
"""

"""
i variable: it keeps changing as we iterate through the loop. 
range: function that takes an argument:

(1,11) ASCENDING --> This will iterate over the loop 10 times one by one.
(1,11,2) --> This will iterate over the loop 10 times but two by two.
(10, 0, -1) DESCENDING--> This will start at 10 and finish at 1. 

Create a program that print Hola 10 times.
"""

# for i in range(1,11,2): 
#     print (f"{i}. Hola")


"""
While the condition is true, it will start executing.
"""
# num = 2

# while num < 10:                     #while number is less than 10 which is true becasue num is set to 1, then...
#     print(f"{num}.This is true.")
#     num += 1                        #This will print the message 9 times because it will stop when num hits 10

"""
Get grades as input from user until they enter -1, once it has finished, print the average of all grades.
"""

# all_grades = []

# while True:
#     grades = int(input("Enter grades: "))

#     if grades == -1:
#         break
#     else:
#         all_grades.append(grades)

# average = sum(all_grades) / len(all_grades)
# print(f"The average is: {average}")

"""
Get number from user, number can only be within range 1 through 10.
Print the multiply table of that number.
"""

while True:
    number = int(input("Enter number to get multiplication table: "))

    if 1 <= number <= 10:
        print("Wrong number. Try again.")
        number = int(input("Enter number to get multiplication table: "))
    
    print(f"Multiplication table of {number}")
    for i in range(1,11):
        print(f"{number} * {i} = {number * i}")



