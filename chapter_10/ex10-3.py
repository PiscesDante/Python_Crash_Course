name_file = open('guest.txt', 'a')
name = input("Enter your name: ")
name_file.write(name + '\n')
print("Your name has been recorded.")