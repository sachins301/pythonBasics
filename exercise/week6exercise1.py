# Exercise 1 – String Methods

#1. Name function (5 points)
def full_name(first_name, last_name, middle_initial):
    first_name = first_name.title()
    last_name = last_name.title()
    middle_initial = middle_initial.title()

    return "{} {} {}".format(first_name, middle_initial, last_name)

print(full_name("John", "Doe", "D"))

#2. String function practice (5 points)
print("Welcome to O\'Neil\'s Boat Rentals!")

sentence = "Hello there!\nHow are you?\nI\'m doing fine."
print(sentence)

string = "hello python"
print(string.upper())

while True:
    age = str(input("Enter you age: "))
    if(age.isdecimal()):
        break

print("Sachin Sudheer".center(25, '*'))


