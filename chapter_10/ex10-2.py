file_object = open('zen_of_python_v2.txt')
for line in file_object :
    print(line.replace('better', 'worse').strip())