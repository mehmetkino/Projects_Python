
welcome = "Welcome to the drinking age test"
print(f"{welcome.upper()}\n")
user_input = input("Would you like to start the test 'y' for yes 'n' for no? ").lower()
while user_input == "y":
    age =int(input("\nPlease enter your age? "))
    if age < 0:
        print(f"You entered {age}.Please enter an valid age!")
    
    elif age >=21 and age <=50 :
        print ("You can legally drink dude!")
    
    else :
        print("\nOhh Man! You are too old to drink!")
        
    user_input= input("\nWould you like to check for another age ? y/n ")
        
       
       
print("\nProgram completed!")       
