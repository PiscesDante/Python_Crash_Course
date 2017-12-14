class User(object) :

    def __init__(self, first_name, last_name) :
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self) :
        print("First Name:", self.first_name.title())
        print("Last Name:", self.last_name.title())

    def greet_user(self) :
        print("Welcome, Mr %s." % (self.first_name.title() + " " + self.last_name.title()))


user1 = User("Davis", "Lee")
user1.describe_user()
user1.greet_user()