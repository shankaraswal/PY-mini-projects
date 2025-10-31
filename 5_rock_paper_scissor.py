import random
from tkinter import E
from turtle import clear

options = ["Rock", "Paper", "Scissor"]

user_choice = input("Please enter Rock, Paper or Scissor: ")
comp_choice = random.choice(options)


print(f"Your choice is {user_choice} and Computer choice is {comp_choice}") 

if user_choice == comp_choice:
   
    print(f"You Chose {user_choice}")
    print(f"Computer Chose {comp_choice}")
    print("\nMATCH TIE -- because both chose same")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("COMPUTER WON")
    else:
        print("YOU WON")
        

elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("YOU WON")
    else:
        print("COMPUTER WON")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("COMPUTER WON")
    else:
        print("YOU WON")


print("\n Start a new game")
print('*******************************************')