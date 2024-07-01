# Exercise 1 – Class Introduction
import random

import functions as func

# #1.1. Import functions: (5 points)
print("25c in farenheit is", func.celsius_to_fahrenheit(25))
print("70f in celsius is", func.fahrenheit_to_celsius(77))

#1.2. NullToBooleanConverter: (5 points)
val1 = None
val2 = "Not Null"
print(func.nullToBooleanConverter(val1))
print(func.nullToBooleanConverter(val2))

# #1.3. Magic 8-Ball: (5 points)
num = random.randint(1,9)
print("Fortune:", func.getAnswer(num))