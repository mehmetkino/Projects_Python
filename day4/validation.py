
for number in range (4):
    print (number)
print("###########")

keep_going = input("please enter 'y' or 'n'? ")

while keep_going == 'y':
    if keep_going != "y":
       keep_going = input("Invalid input! Please enter 'y' or 'n' ")
    else:
        print("Your input was correct")
      
        keep_going = input("Do you want to keep goin? Enter 'y' to keep going or 'n' to quit!")
       
print("Program terminated!")      
    