import json

numbers = [2,3,5,7,11,13]
filename = 'numbers.json'
f_obj = open(filename, 'w')
json.dump(numbers, f_obj)