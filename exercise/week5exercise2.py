# Exercise 2 – Function Arguments and Variables

#2.1. Sum of numbers (3 points)
def sum_of_numbers(numbers):
    return sum(numbers)

print(sum_of_numbers([1, 2, 3, 4, 5]))

#2.2. Number power (3 points)
def number_power(num1, num2):
    return pow(num1, num2)

print(number_power(3,2))

#2.3. Tax function (3 points)
def tax_func(item_price):
    return item_price*1.07

print("Price with Tax:",tax_func(100))

#2.4. Average function (3 points)
def average_func(num1, num2, num3):
    return (num1 + num2 + num3)/3

print("Average:", average_func(3,3,3))