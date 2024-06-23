# week 6 codealong 3

"""
File Open Mode Cheat Sheet:

r = reading, this is the default mode.
r+ = Opens a file for both reading and writing.
w = Opens a file for writing only. Overwrites the file if the file exists.
If the file does not exist, creates a new file for writing.
w+ = Opens a file for both writing and reading.
Overwrites the existing file if the file exists.
If the file does not exist, it creates a new file for reading and writing.
a = Opens a file for appending. The file pointer is at the end of the file if the file exists.
That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
a+ = Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode.
If the file does not exist, it creates a new file for reading and writing.r = reading, this is the default mode.
r+ = Opens a file for both reading and writing.
w = Opens a file for writing only. Overwrites the file if the file exists.
If the file does not exist, creates a new file for writing.
w+ = Opens a file for both writing and reading.
Overwrites the existing file if the file exists.
If the file does not exist, it creates a new file for reading and writing.
a = Opens a file for appending. The file pointer is at the end of the file if the file exists.
That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
a+ = Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode.
If the file does not exist, it creates a new file for reading and writing.
"""


while True:
    file_name = input("Enter a file name: ")
    try:
        fhandle = open(file_name, "r+")
        contents = fhandle.read()
        print(contents)

        while True:
            text = input("What do you want to write out? ")
            if text.lower() == "done":
                break
            fhandle.write(text + "\n")

    except Exception as ex:
        print(ex)
    else:
        break

blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2},
              {'Likes': 13, 'Comments': 2, 'Shares': 1},
              {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3},
              {'Comments': 4, 'Shares': 2},
              {'Photos': 8, 'Comments': 1, 'Shares': 1},
              {'Photos': 3, 'Likes': 19, 'Comments': 3}]

total_likes = 0

for post in blog_posts:
    try:
        total_likes += post['Likes']
    except KeyError:
        # If 'Likes' key is missing, add it with value 0
        post['Likes'] = 0
        total_likes += post['Likes']

print("Total likes:", total_likes)
print("Updated blog posts list:", blog_posts)
