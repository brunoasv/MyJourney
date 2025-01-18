#Error Handling: It will provide an alert to the user if they enter a wrong input or if the program encounters
# an error, but the program will continue running.

# num = 10
# denominator = int(input("Enter a number that's not a 0: "))
# list = []

# try:
#     print("The answer is: " + str(num/denominator))
#     #n = int(input("Enter something: "))
#     print(list[3])
# except ZeroDivisionError:
#     print("You can't divide by 0")
# except ValueError:
#     print("You must enter a number")
# except Exception:
#     print("Unknown error")

# print("Program continues...")

values = [10, 20, 0, 40]
#number = int(input("Enter a number to divide each element by: "))

for value in values:
    try:
        print(value/2)
    except:
        pass