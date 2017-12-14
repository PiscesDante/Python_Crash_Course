file_object = open('guest_book.txt', 'a')
while True :
    name = input('Enter a name: ')
    if name == 'quit' :
        break
    else :
        print('Welcome, %s' % name)
        file_object.write(name + '\n')