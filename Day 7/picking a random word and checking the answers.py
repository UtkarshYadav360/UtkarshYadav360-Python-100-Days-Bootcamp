# HANGMAN GAME :


# THE CODE BELOW IS TO PICK A RANDOM WORD AND CHECK THE LETTERS GIVEN BY USER.

#########################################################################################################
# importing random module
import random

# list of words
word_list = ["adwark","baboon","camel"]

# chosen word
chosen_word = random.choice(word_list)

# user input for guess and turning it into lowercase
guess = input("Guess the letter : ").lower()

# checking if the letter input by user is in the chosen_word
for letter in chosen_word :
    if guess == letter :
        print(f"{letter}, Right")
    else :
        print(f"{letter}, Wrong")
#########################################################################################################
