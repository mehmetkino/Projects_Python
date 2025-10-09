print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/___/____
******************************************************************************* ''')
print("Welcome to the Treasure Island.\nYour mission is to find the treasure!\n")
print("You are at a cross road. Where do you want to go")

direction_1 = input("Type 'left' or 'right' ")
print()
if direction_1 == "left" or direction_1 == "Left" or direction_1=="LEFT":
    print("You've come to a lake. There is an Island in the middle of the lake")
    direction_2 = input("Type 'swim' to swim across or 'wait' to wait for a boat? ")
    print()
    if direction_2 =="wait":
        print("You arrive at the Island unharmed. There is house with 3 doors")
        door_color = input("Choose a door to open!\nType a door color? ")
        print()
        if door_color== "red" or door_color=="Red" or door_color=="RED":
            print("You are burned by fire.\nGame is Over!")
        elif door_color == "blue" or door_color == "Blue" or door_color =="BLUE":
            print("Eaten by beasts.\nGame is over")
        elif door_color =="yellow" or door_color== "Yellow" or door_color =="YELLOW":
            print("You win! You have the treasure now!")
        else:
            print("You picked a wrong door\nGame Over!")       
    else:
        print("Attacked by trout\nGame Over!")    
else:
    print("You fall into a hole!\nGame over!")        




