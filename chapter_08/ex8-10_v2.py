def make_great(magicians_list) :
    new_list = []
    for name in magicians_list :
        name += " the Great"
        new_list.append(name)
    return new_list

def show_magicians(magicians_list) :
    magicians_list = make_great(magicians_list)
    for name in magicians_list :
        print(name)

# =================main function====================

magicians_list = ['mike', 'foo', 'buzz', 'bar']
show_magicians(magicians_list)