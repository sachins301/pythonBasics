# Exercise #1: (5 points)
import datetime
from math import pi, sqrt


# Explain what the following variables refer to, and their scope:
# 1. Person
# <class '__main__.Person'> , scope is this file, global attribute.

# 2. person
# <__main__.Person object at 0x00000211E6C79070> Instance of the class Person, global scope.

# 3.surname
# class variable/parameter of Person. Instance variable accessible only through the class instance. Scope is the class instance.

# 4. self
# self is a keyword that points to the instance of current class. scope is the class instance it is called from.

# 5. age (the function name)
# Class Method of Person, scope is the instance of class. accessed through the instance.

# 6. age
# local variable inside the age method. Scope is the class method.

# 7. self.email
# Instance variable of the class. Scope is the class methods and class instance.

# person.email
# Accessing the email variable of class Person instance person. global scope.


# Exercise #2: (5 points)

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email
        self.age_last_recalculated = None
        self.age = None
        self.recalculate_age()

    def age(self):
        # replace the code in the age function
        if (datetime.date.today() > self.age_last_recalculated):
            self.recalculate_age()
        return self.age

    def recalculate_age(self):
        today = datetime.date.today()
        # todo: set local variable "age", subtract today's year from birthdate year. age = ...
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        # todo: set the age class variable to the new age value calculated from above.
        self.age = age
        # todo: set a new class variable _age_last_recalculated to equal today.
        self.age_last_recalculated = today


person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12),  # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)

print(person.name)
print(person.email)
print(person.age)


# Exercise #3: (5 points)

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


square = Square(3)
print("Area:", square.area())
square.side = 4
print("New Area:", square.area())

# Exercise #4: (5 points)
print(dir(person))

# 1. What happens if you call the __str__ method on the instance? Verify that you get the same result if you call the str function with the instance as a parameter.
print(person.__str__())
print(str(person))
# Since the __str__ method is not defined, the function returns the memory location of the instance of the class.
# Both __str__ and str() returns the same output

# 2. What is the type of the instance?
print(type(person))
# <class '__main__.Person'>

# 3. What is the type of the class?
print(Person)
# <class '__main__.Person'> Instance of the class

# 4. Write a function which prints out the names and values of all the custom attributes of any object that is passed in as a parameter. (see vars() hint.)
print(vars(person))


# Exercise #5: (5 points)
class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        reversed_words = words[::-1]
        reversed_text = ' '.join(reversed_words)
        return reversed_text


sentence = "Hello world"
reverser = StringReverser(sentence)
print("Original sentence:", sentence)
print("Reversed sentence:", reverser.reverse_words())


# Exercise #6: (5 points)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


radius = 5
circle = Circle(radius)
print("Radius of the circle:", radius)
print("Area of the circle:", circle.area())
print("Perimeter of the circle:", circle.perimeter())


# Exercise #7: (5 points)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


length = 5
width = 3
rectangle = Rectangle(length, width)

print("Length of the rectangle:", length)
print("Width of the rectangle:", width)
print("Area of the rectangle:", rectangle.area())


# Exercise #8: (5 points)
class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return sqrt((self.coor2[0] - self.coor1[0]) ** 2 + (self.coor2[1] - self.coor1[1]) ** 2)

    def slope(self):
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())


# Exercise #9: (5 points)

def collatz(number):
    if number % 2 == 0:
        res = number // 2
    else:
        res = 3 * number + 1

    print(res)
    return res


num = int(input("Enter a number:"))
while num != 1:
    num = collatz(num)
