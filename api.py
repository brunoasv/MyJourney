#When entering a URL address in the browser, and the page loads, this will be a considered a GET request. 
import requests

#make a call to the API
data = requests.get('')        #It will grab data from the API
data_formatted = data.json()   #formats data into json form for easier reading
print(data_formatted)          #Prints the whole data in json format

print(data_formatted["name"])  #prints a parameter from the json data




