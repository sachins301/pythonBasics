# Exercise 1: (3 points)
grades = [90,100,70,45,76,84,93,21,36,99,100]
a = b = c = d = f = 0
for grade in grades:
    if grade >= 90:
        a += 1
    elif grade >= 80:
        b += 1
    elif grade >= 70:
        c += 1
    elif grade >= 60:
        d += 1
    else:
        f += 1
print("A: ", a, "; B: ", b, "; C: ", c, "; D: ", d, "; F: ", f)

# Exercise 2: (3 points)
grades = [93, 74, 66, 98, 34, 75, 79, 83, 84, 91, 12, 69, 72]
for i in range(0, len(grades)):
    if grades[i] >= 90:
        continue
    elif grades[i] >= 80:
        grades[i] += 2
    elif grades[i] >= 70:
        grades[i] += 5
    else:
        grades[i] += 8
print("Curved Grades = ", grades)

# Exercise 3: (3 points)
sales = []
for i in range(1, 8):
    sales.append(int(input(f"Enter sales for Day #{i}: ")))
print("Sales for the week: ",sales)

# Exercise #4: (3 points)
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
new_list = my_list[:3]
print(new_list)

new_list = my_list[1:4]
print(new_list)

new_list = my_list[-4:]
print(new_list)

# Exercise #5: (3 points)
products = ["apple", "pear", "peach", "banana"]
if input("Enter a product name: ").strip().lower() in products:
    print("Product is present in inventory")
else:
    print("Product not found")

# Exercise #6: (3 points)
a = [1,2,3,4,5]
b = [2,3,10,11,12,1]
c = []

for i in a:
    if i in b:
        c.append(i)
print(c)

# Exercise #7: (3 points)
names = []
while(True):
    name = input("Enter a first name or \"end\" to exit: ")
    if name.strip().lower() == "end":
        break
    elif name not in names:
        names.append(name)
    else:
        continue
print(names)

# Exercise #8: (3 points)
products = ["apple", "pear", "peach", "banana"]
while(True):
    name = input("Enter a product name or \"end\" to exit: ")
    if name.strip().lower() == "end":
        break
    elif name in products:
        products.remove(name)
        print(products)
    else:
        print("Product not available")

# Exercise #9: (3 points)
products = ['peanut butter', 'jelly', 'bread']
prices = [3.99, 2.99, 1.99]
product = input("Enter a product: ")
print("This product costs: ",prices[products.index(product)])

# Exercise #10: (3 points)
n = int(input("Enter number of students: "))
assn = int(input("Enter number of assignments given: "))
for i in range(1, n+1):
    print("Student #",i)
    avg = 0
    for j in range(1, assn+1):
        avg += int(input(f"Assignment #{j}: "))
    print(f"Student #{i} earned a {avg/assn}")