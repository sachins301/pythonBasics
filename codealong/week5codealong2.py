# week 5
# codealong2

def format_name(first_name, last_name):
    return first_name + " " + last_name

first = input("What is your first name? ")
last = input("What is your last name? ")
formated_name = format_name(first, last)
print(formated_name)

print("Hello", format_name(first, last))

def average(num1, num2, num3):
    results = num3 + num2 + num1
    avg = results/3
    return avg

avg = average(5, 18, 25)
print(avg)

def func(num1, num2):
    if num1 < 0:
        return
    return num1 + num2

print(func(1, 20))
print(func(-1, 20))

def print_dict(dictionary):
    keys = list(dictionary.keys())
    values = list(dictionary.values())

    for i in range(0, len(keys)):
        k = keys[i]
        v = values[i]
        print(k, v)

example_dict = {
    "name": "Thor",
    "age": "25"
}

print_dict(example_dict)

def multiply_by(a=1, b=2):
    return a*b

print(multiply_by())
print(multiply_by(5))
print(multiply_by(5, 3))

def func(value, logging = False):
    if logging:
        print("Logging is on")
    print(value)

func("Calling this function", True)
func("Calling this function")
