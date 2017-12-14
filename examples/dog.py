class Dog(object) :
    def __init__(self, name, age) :
        self.__name = name
        self.__age = age
    
    def sit(self) :
        print(self.__name.title() + ' is now sitting.')
    
    def roll_over(self) :
        print(self.__name.title() + ' rolled over.')

# ==========================================================

my_dog = Dog('willie', 6)
my_dog.sit()
my_dog.roll_over()