favorite_languages = {
    'jan' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'c++'
}

people = ['jan', 'davis', 'kali', 'tom', 'edward']

for person in people :
    if person in favorite_languages.keys() :
        print("Thank you for joining us %s!" % person.title())
    else :
        print("Come on and join us %s!!!" % person.title())