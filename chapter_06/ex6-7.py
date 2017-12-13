person1 = {
    'first_name' : 'telesa',
    'last_name' : 'may',
    'age' : 55,
    'city' : 'london',
}

person2 = {
    'first_name' : 'george',
    'last_name' : 'bush',
    'age' : 78,
    'city' : 'washington',
}

person3 = {
    'first_name' : 'tony',
    'last_name' : 'blair',
    'age' : 60,
    'city' : 'London',
}

peeple = [person1, person2, person3]

for person in peeple :
    print("Name:", person['first_name'].title() + " " + person['last_name'].title())
    print("Age:", person['age'])
    print("Location:", person['city'], '\n')