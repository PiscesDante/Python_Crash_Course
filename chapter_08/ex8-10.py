def make_great(magicians_name) :
    magicians_name += ' the Great'
    return magicians_name

def show_magicians(magicians_list) :
    for name in magicians_list :
        name = make_great(name.title())
        print(name)

def main() :
    magicians_list = ['mike', 'foo', 'buzz', 'bar']
    show_magicians(magicians_list)

# =================main function====================

main()