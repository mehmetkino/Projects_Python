print("Welcome to tip calculator!")
total_bill= float(input("How much was the total bill? $"))

tip= float(input("How much tip whould you like give? 10, 12 or 15? "))
tip_amount = total_bill*(tip/100)

number_of_people = int(input("How many people to split the bill? "))

each_person_pay = (total_bill+tip_amount)/number_of_people

print(f"Each person should pay: $ {each_person_pay}")