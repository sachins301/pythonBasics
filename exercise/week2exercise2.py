#1. Password verification (2 points)

password = "Utes!"
user_password = str(input("Enter the password: "))
if user_password == password:
    print("Access Granted!")
else:
    print("Access Denied!")


#2. Voting Age (2 points)
voting_age = 18
user_age = int(input("How old are you? "))
if user_age >= voting_age:
    print("You are eligible to vote!")
else:
    print(f"You have {voting_age - user_age} years more to go.")

#3. Dress for Weather (2 points)
temp = int(input("What is the temperature? "))
if temp < 40:
    print("Wear a warm coat.")
elif temp < 70:
    print("Wear a light jacket.")
elif temp < 100:
    print("Wear something cool.")
else:
    air_conditioning = input("Do you have air conditioning at home? (yes/no) ")
    if air_conditioning == 'yes':
        print("Stay at home.")
    else:
        print("Bummer, try a swimming pool.")
