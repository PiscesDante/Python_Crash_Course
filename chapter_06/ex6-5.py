river_country = {
    'nile' : 'egypt',
    'missisibi' : 'usa',
    'amazon' : 'brazil',
    'yangtzi' : 'china',
}

for river, country in river_country.items() :
    print("The %s runs through %s" % (river.title(), country.title()))
print("")

for river in river_country.keys() :
    print(river.title())
print("")

for country in river_country.values() :
    print(country.title())