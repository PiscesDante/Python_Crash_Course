import json

username = input("What is your name: ")
filename = 'username.json'
file_object = open(filename, 'w')
json.dump(username, file_object)
print("We'll remember you when you come back, " + username + "!")