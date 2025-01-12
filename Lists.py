# for loops are used to iterate over a sequence (a list, a tuple, a dictionary, a set, or a string).

# cities = ["New York", "London", "Paris", "Tokyo", "Sydney"]

# for city in cities:
#     print(city)


# numbers =[]
# numbers.append(1) 
# numbers.append(2)                # append => it adds 2 to the list after 1
# numbers.append(14)
# numbers.append(99)
# numbers.append("Mark") 
# numbers.pop()                    # pop => it removes the last element from the list

# print(numbers)
# print(numbers[1])                # prints the second element in the list
# print(len(numbers))               # prints the length of the list


"""
get numbers from user until user enters -1
save numbers in a list
When user is done print each number mutiplied by 100
"""

# mynumbers = []
# numbers = int(input("Enter a number to add to the list and when done enter -1: "))

# while numbers != -1:           # while the number entered by the user is not -1, then it will keep asking for a number
#     mynumbers.append(numbers)
#     numbers = int(input("Enter a number to add to the list and when done enter -1: "))

# for number in mynumbers:
#     print(number * 100)

"""
Delete a specific element from a list
print the index of the first number 3 in the list
sort the list in ascending order
reverse the list
enumarate the list of elements when printing

"""

# mylist = [3,4,3,23,4,3,2,3,4,5,6,4,2,3,4,5,3,1,2,3]
# print(mylist)

# # for n in mylist:
# #     if n == 3:
# #         mylist.remove(n)
# # print(mylist)

# print(mylist.index(23)) 
# mylist.sort()           
# print(mylist)   
# mylist.reverse()
# print(mylist)           


numbers = [234,54,1,2356,645,23,2,2,2,2,2,2,2]

for i, n in enumerate(numbers):
    print(f"{i}. {n}")

print(numbers.count(2))
   




