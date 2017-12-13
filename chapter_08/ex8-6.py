def city_country(city = 'Shanghai', country = 'China') :
    res = city.title() + ', ' + country.title()
    return res

print(city_country())
print(city_country('new york', 'america'))
print(city_country('beijing'))