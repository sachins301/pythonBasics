#1 Sum of Positive Numbers (3 points)

total_sum = 0
usr_input = int(input("Enter a number: "))
while(usr_input != 0):
    if usr_input > 0:
        total_sum += usr_input
    usr_input = int(input("Enter a number: "))

print("Total sum: ",total_sum)

#2 Temperature Converter (3 points)

total_tempC = 0
count = 0
temp = input("Enter a temperature in Fahrenheit or \"done\": ")

while(temp != "done"):
    temp = float(temp)
    temp = (temp - 32) * 5/9
    total_tempC += temp
    count += 1
    temp = input("Enter a temperature in Fahrenheit or \"done\": ")

avg_temp = total_tempC/count
print(f"Average Temperature: {avg_temp:.3f}°C")