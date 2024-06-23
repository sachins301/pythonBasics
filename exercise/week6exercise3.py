#Exercise 5 – Files & Error Handling

#1. Exception handling (5 points)
while True:
    try:
        num = int(input("Input an integer: "))
    except:
        print("Invalid Integer")
    else:
        break

#2. File IO (5 points)

fhandle = open("test.txt", "w+")
contents = fhandle.read()
print(contents)

while True:
    text = input("What do you want to write out? ")
    if text.lower() == "done":
        break
    fhandle.write(text + "\n")

#3. Name (5 points)
file_name = input("Enter a file name: ")
try:
    fhandle = open(file_name, "r+")
    contents = fhandle.read()
    print(contents)

except Exception as ex:
    print("File was not found.", ex)
