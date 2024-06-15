#1.1. Hello World (again) (3 points)

def hello_world():
    name = input("What is your name? ")
    print(f"Hello, {name}")
hello_world()

#1.2. Dog Years (3 points)
def dog_years():
    dog_age = int(input("What is the age of your dog? "))
    dog_years_age = dog_age * 7
    print(f"Your dog is {dog_years_age} years old in dog years.")

dog_years()

#1.3. Purchase (3 points)
def purchase():
    num_items = int(input("Enter the number of items to purchase: "))
    print(f"You have chosen to purchase {num_items} items.")

purchase()