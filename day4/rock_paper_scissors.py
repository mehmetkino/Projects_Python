#Create a program to play rock paper scissor game against computer!
import random

game = ["rock","paper","scissors"]

user_choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print("You chose ", user_choice)

computer_choice = random.randint(0,2)
print("Computer chose", computer_choice)

if user_choice >= 3 or user_choice <0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif computer_choice == 0 and user_choice ==2:
    print("Computer wins!")
elif computer_choice < user_choice:
     print("You win!")
elif computer_choice > user_choice :
    print("Computer wins!")
elif computer_choice == user_choice:
    print("It is a draw!")
    
else:
    print("You typed an invalid number. You lose!")




