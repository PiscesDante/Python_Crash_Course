def make_great(magicians_list) :
    new_list = magicians_list[:]
    for name in new_list :
        name = name + " the Great"
    return new_list

def show_magicians(magicians_list) :
    return make_great(magicians_list)

if __name__ == "__main__" :
    magicians_list = ['mike', 'foo', 'buzz', 'bar']
    new_list = show_magicians(magicians_list)
    print(new_list)
    print(magicians_list)