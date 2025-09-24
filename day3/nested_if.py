#Mehmet Kino
#nested if
#This program will check whether a person can ride a rollercoaster or not.

bill= 0
print("welcome to the rolercoaster")
height = int(input("\nWhat is your height in cm? "))

if height >=120:
    print("\nYou can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <=12:
        bill = 5
        print("\nPlease pay $5.")
    elif age <= 18:
        bill = 7
        print("\nPlease pay $7.")
    else:
        bill = 12
        print("\nPlease pay $12.")

    wants_photo= input("Do you want to have a photo take? Type y for Yes n for No ")
    if wants_photo == "y":
        #add $3 dollars to their bill
        bill = bill +3 #bill +=3
    print(f"Your final bill is {bill}")    



else:
    print("\nYou cannot ride the rollercoaster")