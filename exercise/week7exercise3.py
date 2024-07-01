# Exercise 3 – Class & Constructors

#3.1. NumberSet Class (5 points)
class NumberSet:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

t = NumberSet(6, 10)
print(t.num1, t.num2)


#3.2. Animal Class (5 points)
class Animal:

    def __init__(self, arms, legs):
        self.arms = arms
        self.legs = legs

    def limbs(self):
        return self.arms + self.legs
    def get_arms(self):
        return self.arms

    def get_legs(self):
        return self.legs

spider = Animal(4,4)
spidlimbs = spider.limbs()
print("Total limbs:",spidlimbs)


#3.3. Cereal Class (5 points)
class Cereal:
    def __init__(self, name: str, brand: str, fiber: int):
        self.name = name
        self.brand = brand
        self.fiber = fiber

    def __str__(self):
        return f"{self.name} cereal is produced by {self.brand} and has {self.fiber} grams of fiber in every serving!"

c1 = Cereal("Corn Flakes", "Kellogg's", 2)
c2 = Cereal("Honey Nut Cheerios", "General Mills", 3)

print(c1)
print(c2)

"""class called Cereal that accepts three inputs in the Ctor: 2 strings and 1 
integer, and assigns them to 3 instance variables in the constructor: 
name, brand, and fiber."""