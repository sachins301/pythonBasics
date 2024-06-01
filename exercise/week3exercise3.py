# Week 3: In-class exercise 3 - for loops

# 3.1 Input with a for-loop (4.5 points)

n = int(input("How many numbers would you like to add? "))
total = 0
for i in range(0, n):
    total += int(input("Enter a number to add: "))
print(total)

#3.2 Find the vowels – for loop (4.5 points)
string = input("Enter a word/sentence: ")
total = 0
for char in string.strip().lower():
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':

        total += 1
print(total)