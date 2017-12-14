from car import Car

# ===============ElectricCar Begin=================

class ElectricCar(Car) :

    def __init__(self, make, model, year) :
        super().__init__(make, model, year) # 初始化父类属性
        self.battery_size = 70

    def describe_battery(self) :
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

# ================ElectricCar End==================

# ============main function=============
my_tesla = ElectricCar('tesla', 'model s', '2016')
print(my_tesla.get_discriptive_name())
my_tesla.describe_battery()