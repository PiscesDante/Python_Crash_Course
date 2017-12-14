import json

filename = "favorite_number.json"

number = int(input("Enter your favorite number: "))
file_obj = open(filename, 'w')
json.dump(number, file_obj)
file_obj.close()

file_obj = open(filename, 'r')
number = json.load(file_obj)
print("I know your favorite number! It's %d." % number)