users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}

# 遍历其中的元素
# for key in users.keys() :
#     print(key)
#     for key, value in users[key].items() :
#         print("  %s | %s" % (key, value))

for key, value in users.items() :
    full_name = value['first'].title() + " " + value['last'].title()
    location = value['location'].title()
    print("Username:", key)
    print("  Full name:", full_name)
    print("  Location:", location, '\n')