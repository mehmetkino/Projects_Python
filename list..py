answer = input("Would you like to create a list of states ? Type yes or no? ").lower()
list_of_states=[]
if answer == "yes":
     print("he said yes")
     add_state = input("What state whould you like to add?  ")
     list_of_states.append(add_state)
     print("The list is: ",list_of_states)
else:
    print("he said no")    

                    