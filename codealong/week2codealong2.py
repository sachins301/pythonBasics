# Week2
# Code along 2

print(True)
print(False)
print(type(True))
print(1 == 1)
print(1 == 2)
print(1 != 1)
print(1 != 2)
print(1 < 2)
print(1 > 2)
print(1 > 2 and 2 < 5)
print(1 > 2 or 2 < 5)
print(not 1 > 2 and not 2 < 5)

a = 1
b = 2
c = 5

print(a == b)
print(a > b and b > c and b)

#part 2
x = 5
if x > 0:
    print("x is positive")
else:
    print("x is less than 0")

x = -1
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero!")
else:
    print("x is less than 0")

x = 0
if x > 0:
    print("x is positive")

    if x % 2 == 0:
        print("This is an even number!")
    else:
        print("Numer is odd!")
else:
    print("Not a positive number")

voting_age = 18
user_age = int(input("How old are you? "))
if user_age >= voting_age:
    print("You are eligibe to vote!")
else:
    print(f"You have {voting_age - user_age} years more to go.")

