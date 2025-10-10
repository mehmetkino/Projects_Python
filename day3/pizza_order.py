print("Welcome to the Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extre_cheese= input("Do you want extra cheese on your pizza? Y or N")

small_pizza = 15
medium_pizza = 20
large_pizza = 25
total_bill = 0

#check what size they want
if size == "S" or size=="s":
    total_bill = small_pizza
elif size =="M" or size=="m":
    total_bill= medium_pizza
elif size == "L" or size=="l":
    total_bill = large_pizza       
    
else:
    print("You typed the wrong input")            

#check whether they want pepperoni or not! it is extra $2 for small and $3 for large
if pepperoni =="Y" or "y":
    if(size == "S"):
        total_bill +=2
    else:
        total_bill+=3


#check if they want extra cheese for $2
if (extre_cheese =="y" or extre_cheese == "Y"):
    total_bill+=1

    
print(f"Your final bill is ${total_bill}")    
