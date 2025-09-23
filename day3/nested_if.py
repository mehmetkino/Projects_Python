#Mehmet Kino
#nested if
#This program will check whether a person can ride a rollercoaster or not.

print("welcome to the rolercoaster")
height = int(input("\nWhat is your height in cm? "))

if height >=120:
    print("\nYou can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <=12:
        print("\nPlease pay $5.")
    elif age <= 18:
        print("\nPlease pay $7.")
    else:
        print("\nPlease pay $12.")
else:
    print("\nYou cannot ride the rollercoaster")