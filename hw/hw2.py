# Exercise 2.1: (2.5 points)
import random

coin = int(input("What is the coin value? "))
if coin == 1:
    print("That's a penny!")
elif coin == 5:
    print("That's a nickle!")
elif coin == 10:
    print("That's a dime!")
elif coin == 25:
    print("That's a quarter!")
elif coin == 50:
    print("That's half dollar!")
else:
    print("That's not a valid coin!")


# Exercise 2.2: (2.5 points)
integer = int(input("Enter an integer value: "))
if integer % 4 == 0 and integer % 3 == 0:
    print("Integer is a multiple of both 4 and 3")
elif integer % 3 == 0:
    print("Integer is a multiple of 3")
elif integer % 4 == 0:
    print("Integer is a multiple of 4")
else:
    print("Integer is neither a multiple of 4 nor 3")

# Exercise 2.3: (2.5 points)

age = int(input("Enter your age: "))
while age <= 0:
    print("Enter a positive value greater than 0")
    age = int(input("Enter your age: "))
if age >= 65:
    print("You receive a discount of 30%")
elif age < 18:
    print("You receive a discount of 15%")
else:
    print("You do not receive any discount")

# Exercise #2.4: (2.5 points)
start = int(input("Enter a starting integer: "))
end = int(input("Enter an ending integer: "))
oddeven = input("Enter odd or even: ")

if oddeven == "odd":
    if start % 2 == 0:
        start += 1
else:
    if start % 2 != 0:
        start += 1

while start <= end:
    print(start)
    start += 2

# Exercise #2.5: (3 points)
nos = int(input("Enter the number of products: "))
total = 0
count = 1
while(count <= nos):
    total += float(input(f"Enter price for product #{count}: "))
    count += 1
print("Total cost: ",total)

# Exercise #2.6: (3 points)   and    Exercise #2.7: (3 points)
flag = "yes"
saved = 0
while flag == "yes":
    price = float(input("Enter the book price: "))
    discounted = price * 0.9
    saved += (price - discounted)
    print(f"Discounted Price: {discounted}")
    flag = input("Do you want enter another price (yes/no)? ")
print("Total amount saved: ",saved)


# Exercise #2.8: (3 points)
capital = "delhi"
while(True):
    ans = input("Enter the capital of India: ").strip().lower()
    if capital == ans:
        print("Correct!")
        break

# Exercise #2.9: (3 points)
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
flag = True
while flag:
    ans = int(input(f"What is {num1} + {num2} = "))
    if ans == (num1 + num2):
        print("Correct!")
        flag = False
    else:
        print("Incorrect, Try again.")

