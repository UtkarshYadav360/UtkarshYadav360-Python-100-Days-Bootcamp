# ROCK,PAPER,SCISSORS GAME :





# rock,paper,scissors ascii art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# greeting to the user
print("Welcome To The Rock,Paper,Scissors Game!\n")

# user choice
user_choice = int(input("What would you choose? Type 0 for Rock, 1 for Paper, 2 for scissors."))

# importing random
import random

# computer choice
computer_choice = random.randint(0,2)

# list of choices
choices = [rock,paper,scissors]

# conditions for the game
# match tie conditon :
if user_choice == computer_choice :
    print(f"YOU CHOOSE :\n{choices[user_choice]}\nCOMPUTER CHOOSE :\n{choices[computer_choice]}")
    print("It's A Tie!")

# user win conditions :
elif user_choice == 0 and computer_choice == 2:
    print(f"YOU CHOOSE :\n{rock}\nCOMPUTER CHOOSE :\n{scissors}")
    print("You Win!")
elif user_choice == 1 and computer_choice == 0 :
    print(f"YOU CHOOSE :\n{paper}\nCOMPUTER CHOOSE :\n{rock}")
    print("You Win!")
elif user_choice == 2 and computer_choice == 1 :
    print(f"YOU CHOOSE :\n{scissors}\nCOMPUTER CHOOSE :\n{paper}")
    print("You Win!")

# computer win conditions
elif user_choice == 2 and computer_choice == 0 :
    print(f"YOU CHOOSE :\n{scissors}\nCOMPUTER CHOOSE :\n{rock}")
    print("You Lose!")
elif user_choice == 0 and computer_choice == 1 :
    print(f"YOU CHOOSE :\n{rock}\nCOMPUTER CHOOSE :\n{paper}")
    print("You Lose!")
elif user_choice == 1 and computer_choice == 2 :
    print(f"YOU CHOOSE :\n{paper}\nCOMPUTER CHOOSE :\n{scissors}")
    print("You Lose!")

# error condition :
else :
    print("Sorry! You typed something wrong.")
