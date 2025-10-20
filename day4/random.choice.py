#This program will focus on random.choice()

import random

car_makes=["honda","toyota", "lincoln","lexus","mazda"]

pick_a_car = "y"
while pick_a_car.lower() == "y" :
    picking_random_car = random.choice(car_makes)
    if picking_random_car == "honda":
        print("You picked Honda\nThat is relaible car\n")
    elif picking_random_car =="toyota":
        print("You picked toyota\nThat is wonderful car make\n")    
    elif picking_random_car =="lincoln":
        print("You picked lincoln\nThat is luxury car\n")    
    elif picking_random_car== "mazda":
        print("You picked Mazda!\nThat is my first car!")
    elif picking_random_car == "lexus":
        print("You picked lexus!\nit is aweome car\n")
    pick_a_car = input("\nDo you want to continue? y/n ")
print("Program Complete!")              


