# Exercise #1: (6 points)

user_word = input("Enter a word in english: ")
dictionary = []
try:
    # open a file for reading
    myvar = open("most_popular_words_in_english.txt", "r")
    contents = myvar.read()
    dictionary = contents.split("\n")

# an error occurred!  handle it here
except:
    print ("Something went wrong!")
else:
    if user_word in dictionary:
        print("The word entered is a popular one in english")
    else:
        print("The word is not popular")

# Exercise #2: (6 points)
username = input("Enter username: ")
password = input("Enter the password: ")
try:
    sec_file = open("security.txt", "w+")
    sec_file.write(username+"\n")
    sec_file.write(password+"\n")
    sec_file.close()
except:
    print("File Exception.")

# Exercise #3: (6 points)
file_username = ''
file_password = ''
try:
    sec_file = open("security.txt", "r")
    contents = sec_file.read().split("\n")
    file_username = contents[0]
    file_password = contents[1]
except:
    print("File Exception.")

username = input("Enter username: ")
password = input("Enter the password: ")

if username == file_username and password == file_password:
    print("Access granted!")
else:
    print("Username or password invalid.")


# Exercise #4: (6 points)
scores = []
try:
    fhandle = open("testscores.txt", "r")
    for score in fhandle.readlines():
        if score.strip().isnumeric():
            scores.append(int(score))
except:
    print("File Exception.")
else:
    print("Average score:", sum(scores)/len(scores))


