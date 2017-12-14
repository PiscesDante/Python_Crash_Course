file_object = open('zen_of_python.txt')
# contents = file_object.read()
# for line in contents :
#     print(line)

for line in file_object :
    print(line.strip())