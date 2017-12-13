def make_car(brand, location, **car_info) :
    ret = {}
    ret['Brand'] = brand.title()
    ret['Location'] = location.title()
    for key, value in car_info.items() :
        ret[key] = value
    return ret

# =============main function==============

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)