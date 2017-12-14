import json

filename = 'numbers.json'
f_obj = open(filename, 'r')
numbers = json.load(f_obj)
print(numbers)
f_obj.close()