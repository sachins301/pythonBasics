import random


# Exercise #1: (5 points)
def topOrBottom():
    print ("#####")

def second():
    print("#   #")

def third():
    print(" # # ")

def mid():
    print("  #  ")

topOrBottom()
second()
third()
mid()
third()
second()
topOrBottom()

# Exercise #2: (5 points)
def feet_to_inches(ft):
    print(f"... {12*ft} inches")

def feet_to_meters(ft):
    print(f"... {ft * 0.3048:.4f} meters")

for i in range(10):
    print(f"{i} ft:")
    feet_to_inches(i)
    feet_to_meters(i)

# Exercise #3: (5 points)
def roll_dice(sides):
    roll1 = random.randint(1, sides)
    roll2 = random.randint(1, sides)
    return sorted([roll1, roll2])

# Rolling 5 sets of dice with different sides
sides_list = [6, 7, 8, 9, 10]
for sides in sides_list:
    roll1, roll2 = roll_dice(sides)
    print(f"{sides} sided dice roll: {roll1} & {roll2}")

# Exercise #4: (5 points)
# This is a guess the number game.
# use the random.randint() function to generate a random number between 1 and 20.
secretNumber = random.randint(1, 20)

print('I am thinking of a number between 1 and 20.')

guess = 0
guesses = 0
# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    guess = int(input("Take a guess. "))
    if guess == secretNumber:
        print(f"Good job! You guessed my number in {guessesTaken} guesses!")
        break
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
    guesses = guessesTaken

if guesses >= 6:
    print(f"Nope. The number I was thinking of was {secretNumber}")