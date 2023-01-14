# HANGMAN GAME :



# importing random module
import random

# list of words
word_list = ["adwark","baboon","camel"]

# chosen word
chosen_word = random.choice(word_list)

# THE CODE BELOW MAKES A LIST WITH BLANK SPACES.

# creating an empty list
display = []

# iterating to the characters in the 'chosen_word' :
for char in range(1,len(chosen_word)+1) :
    # each time the loop run "_" will be appended to the list called 'display'
    display.append("_")
print(char)



#########################################################################################################
# here the value of the variable is False, which shows the game is not over yet.
end_of_game = False

# loop will run till the game is not over
while not end_of_game:
    # user input for guess and turning it into lowercase
    guess = input("Guess the letter : ").lower()

# THE CODE BELOW REVEALS THE CORRECT LETTER IN THE LIST NAMED 'display' :

    # loop will run as many times there are letters in the word and it gives us the position or index of the letters to work with
    for position in range(len(chosen_word)) :
        # variable named 'letter' contains the letter from the position or index of the 'chosen_word'
        letter = chosen_word[position]
        # condition;
        if letter == guess :
            # if the above condition is true, then the 'letter' will be placed to its position in the list 
            display[position] = letter

    # printing the 'display' list with the correct filled letters if the user is able to guess them right
    print(display)

    # checking if '_' is not present in the list named 'display'
    if '_' not in display :
        # if the above condition is true then the game will be over becasue user guessed all the letters.
        end_of_game = True
        # prints when the user wins
        print("You Win!")

# Here the "while loop that continously takes the user input to guess the letter", will stop here because the game will end after the above condition is true.
#########################################################################################################
