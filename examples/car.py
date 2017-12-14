# ==================Car Begin=====================

class Car(object) :

    def __init__(self, make, model, year) :
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_discriptive_name(self) :
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self) :
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, new_odometer) :
        if new_odometer >= self.odometer_reading :
            self.odometer_reading = new_odometer
        else :
            print("Error: Cannot roll back an odometer.")

    def increment_odometer(self, miles) :
        self.odometer_reading += miles

# ===================Car End=======================

# =========main function==========

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_discriptive_name())
# my_new_car.read_odometer()

# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

# my_used_car = Car('subaru', 'outback', 2013)
# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()