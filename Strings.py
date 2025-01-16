# nombre = "1"             
# print(nombre.isdigit()) # Tell me if a string is a difit or not. Returns True or False

# nombre = "Bruno"

# x = nombre.index("o")            # Find the index of a letter in a string. 
# list = ["Liverpool", "Inter"]  

# print(x) # 4
# print(list.index("Inter"))       # Find the index of an element in a list.

# phrase = "I am done studying for the day"
# print(phrase.endswith("day"))                # Check if a string ends with a specific word. Returns True or False
# print(phrase.upper())                        # Convert a string to uppercase  
# print(phrase.lower())                        # Convert a string to lowercase
# print(phrase.islower())                      # Check if a string is in lowercase. Returns True or False
# print(phrase.replace("studying", "working")) # Replace a word in a string with another word.
# print(phrase.replace(" ", "-"))              # Replaces spaces for a hyphen.
# print(phrase.count("a"))                     # Count the number of times a letter appears in a string.




credentials = "Bruno,1234!"

info = credentials.split(",")                  # Split a string into a list.
print(info) 

username = info[0]
password = info[1]

print(f"username: {username}")
print(f"password: {password}")                  




