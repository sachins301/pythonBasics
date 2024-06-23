# Exercise 2 – Exception Handling

#1. Divide by zero exception (5 points)
def divide(num1, num2):
    try:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
        return result
    except ZeroDivisionError:
        print("Invalid argument")

divide(1, 2)
divide(1, 0)


#2. Basic exception handling (5 points)
try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except:
    print("Invalid operation")

#3. try-except-finally (5 points)
try:
    x = 5
    y = 0
    z = x / y
except:
    print("Invalid operation")
finally:
    print("All Done")

#4. try-except-else(5 points)

def square(num):
    return num*num

while True:
    try:
        num = int(input("Input an integer: "))
        print("Thank you, your number squared is:",square(num))
    except:
        print("An error occurred! Please try again!")
    else:
        break


