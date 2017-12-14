class Restaurant(object) :
    
    def __init__(self, restaurant_name, cuisine_type) :
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self) :
        print("Name:", self.restaurant_name.title())
        print("Cuisine Type:", self.cuisine_type.title())

    def open_restaurant(self) :
        print("The restaurant is open now.")

    def set_number_served(self, new_number) :
        if new_number >= self.number_served :
            self.number_served = new_number
    
    def increment_number_served(self, increased_number) :
        if increased_number > 0 :
            self.number_served += increased_number


class IceCreamStand(Restaurant) :

    def __init__(self, restaurant_name, cuisine_type) :
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'stawberry', 'vanilla', 'cheese']

    def show_the_flavers(self) :
        print("Here are the current flavor:")
        for flavor in self.flavors :
            print(" -%s" % flavor.title())


stand1 = IceCreamStand('Diary Queen', 'ice cream')
stand1.describe_restaurant()
stand1.show_the_flavers()