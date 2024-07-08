
# #1.1. Ice Cream Shop inherits from Restaurant (5 points)
class Restaurant:

    def __init__(self, name, cuisine_type):
        self.restaurant_name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant Name:", self.restaurant_name)
        print("Cuisine Type:", self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " is open for business")

restaurant = Restaurant("New World", "French")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()


class IceCreamStand (Restaurant):
    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.flavors = flavors

    def get_flavors(self):
        print("Flavors:", self.flavors)

ice_cream = IceCreamStand("My Ice Cream Shoppe", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry"])
ice_cream.describe_restaurant()
ice_cream.open_restaurant()
ice_cream.get_flavors()



# #1.2. Admin inherits from User (5 points)

class User:
    def __init__(self, first_name, last_name, email, username, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.age = age
        self.location = location


    def describe_user(self):
        print(f"User Information:\n"
              f"Name: {self.first_name} {self.last_name}\n"
              f"Email: {self.email}\n"
              f"Username: {self.username}\n"
              f"Age: {self.age}\n"
              f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")

user1 = User("Jane", "Doe", "jane.doe@example.com", "janedoe92", 30, "New York")
user2 = User("John", "Dow", "john.doe@example.com", "johndoe77", 45, "California")


user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()


class Admin(User):
    def __init__(self, first_name, last_name, email, username, age, location):
        super().__init__(first_name, last_name, email, username, age, location)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"Admin Privileges:", self.privileges)

admin = Admin("Sachin", "Sudheer", "sachin.sudheer301@gmail.com", "admin", 26, "Salt Lake City")
admin.describe_user()
admin.greet_user()
admin.show_privileges()
