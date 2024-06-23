# week 6
# code along lab 2
number_of_scores = 0
try:
    number_of_scores = int(input("Enter how many scores: "))
except:
    print("Invalid value")
scores = []
for x in range(0, number_of_scores):
    while True:
        try:
            score = int(input("What is the score # " + str(x+1)))
            scores.append(score)
        except:
            print("Invalid score value, Please try again.")
        else:
            break

    try:
        print(sum(scores)/0)
    except Exception as ex:
        print("An error occured.", ex)

while True:
    try:
        email = input("Enter an email address")
        parts = email.split("@")
        name = parts[0]
        domain = parts[1].split(".")
        print("The email address is:", name, domain[0], domain[1])
        print("Thank you")
        break
    except:
        pass