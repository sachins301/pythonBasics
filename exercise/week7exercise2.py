# Exercise 2 – Class Introduction
from math import pi


# 2.1. The simplest class: (5 points)
class Simplest:
    pass


# a. Using the code below, what type is this object?
print(type(Simplest))
# <class 'type'>

# b. Create an instance of Simplest to a variable called simp. What type is simp?
simp = Simplest
print(type(simp))


# <class 'type'>

# 2.2. Person Class: (5 points)
class Person:
    first_name = ""
    middle = ""
    last_name = ""

    def format_name(self):
        return "{} {} {}".format(self.first_name, self.middle, self.last_name)


person = Person()
person.first_name = "Sachin"
person.middle = ""
person.last_name = "Sudheer"
print(person.format_name())


# 2.3. Cylinder: (5 points)
class Cylinder:

    def set_height_radius(self, height, radius):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * pi*(self.radius)**2

    def surface_area(self):
        top = pi * self.radius**2
        return 2*top + (2*pi*self.radius*self.height)

mycyl = Cylinder()
mycyl.set_height_radius(2,3)
print(mycyl.volume())
print(mycyl.surface_area())
