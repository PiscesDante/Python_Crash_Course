file_name = input('Enter a file name: ')
file_object = open(file_name, 'w')
while True :
    line = input('> ')
    if line == 'quit' :
        break
    else :
        line += '\n'
        file_object.write(line)
file_object.close()