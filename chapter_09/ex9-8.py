class User(object) :

    def __init__(self, first_name, last_name) :
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self) :
        print("First Name:", self.first_name.title())
        print("Last Name:", self.last_name.title())

    def greet_user(self) :
        print("Welcome, Mr %s." % (self.first_name.title() + " " + self.last_name.title()))

    def increment_login_attempts(self) :
        self.login_attempts += 1
    
    def reset_login_attempts(self) :
        self.login_attempts = 0


class Privileges(object) :

    def __init__(self) :
        self.privileges = ['can add post', 'can delete post', 'can ban user']


class Admin(User) :
    
    def __init__(self, first_name, last_name) :
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
    
    def show_privileges(self) :
        print("Here are the privileges of admin:")
        for privilege in self.privileges.privileges :
            print("-%s" % privilege.title())


admin = Admin('Davis', 'Lee')
admin.describe_user()
admin.greet_user()
admin.show_privileges()