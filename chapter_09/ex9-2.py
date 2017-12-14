class Restaurant(object) :
    
    def __init__(self, restaurant_name, cuisine_type) :
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self) :
        print("Name:", self.restaurant_name.title())
        print("Cuisine Type:", self.cuisine_type.title())

    def open_restaurant(self) :
        print("The restaurant is open now.")


my_restaurant = Restaurant("Xin Hua", "Chinese")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()