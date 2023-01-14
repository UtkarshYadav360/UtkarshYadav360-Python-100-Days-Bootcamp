# HANGMAN GAME :



# importing random module
import random

# logo of the game
logo = ''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       '''

# greeting to the user
print(logo,"\n")
print("Welcome To The Hangman Game!")
print("Save The Hangman By Choosing The Correct Animal Name!")

# stages of hangman
stages =  ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# list of words
animal_list = ["ant", "baboon", "bear", "beaver", "camel", "cat", "cobra", "cougar",
        "coyote", "crow", "deer", "dog", "donkey", "duck", "eagle", "fox", "frog", "goat",
        "goose", "hawk", "lion", "lizard", "llama", "monkey", "moose", "mouse", "mule",
        "owl", "panda", "parrot", "pigeon", "python", "rabbit", "rat",
        "rhino", "salmon", "seal", "shark", "sheep", "sloth", "snake", "spider",
        "swan", "tiger", "toad", "trout", "turkey", "turtle", "weasel", "whale", "wolf",
        "wombat", "zebra"]

# chosen word
chosen_word = random.choice(animal_list)

#########################################################################################################
# total lives of the player
lives = 6

# printing the hangman on its first stage
print(stages[6])

# creating an empty list
display = []

# iterating to the characters in the 'chosen_word' :
for char in range(1,len(chosen_word)+1) :
    # each time the loop run "_" will be appended to the list called 'display'
    display.append("_")

# here the value of the variable is False, which shows the game is not over yet.
end_of_game = False

# loop will run till the game is not over
while not end_of_game:
    # user input for guess and turning it into lowercase
    guess = input("Guess the letter : ").lower()

    # checks if the user already guessed the letter
    if guess in display :
        # this will be printed if the above statement is true
        print(f"You've already guessed {guess}.")

    # loop will run as many times there are letters in the word and it gives us the position or index of the letters to work with
    for position in range(len(chosen_word)) :
        # variable named 'letter' contains the letter from the position or index of the 'chosen_word'
        letter = chosen_word[position]
        # condition;
        if letter == guess :
            # if the above condition is true, then the 'letter' will be placed to its position in the list 
            display[position] = letter

# condition; 
# checks if the guess is not in 'chose_word'
    if guess not in chosen_word :
        # then deduct one life each time from the total lives of the user
        lives-=1
        # if the user guessed the wrong letter then this message will be printed
        print(f"You guessed {guess}, that's not in the animal name.")
        # condition; if lives becomes 0, all lives are finished
        if lives == 0 :
            # if the above nested if statement is true then the game will over
            end_of_game = True
            # then, player will lose if game overs
            print("You Lose!")
            # printing the chosen word
            print(f"You Have To Guess {chosen_word}.")

    # joining all the elements in the list and turn it into a string.
    print(f"{' '.join(display)}")

    # checking if '_' is not present in the list named 'display'
    if '_' not in display :
        # if the above condition is true then the game will be over becasue user guessed all the letters.
        end_of_game = True
        # prints when the user wins
        print("You Win!")

# Here the "while loop that continously takes the user input to guess the letter", will stop here because the game will end after the above condition is true or 'lives' becomes 0.

    # printing stages of the hangman according to the 'lives' left of the user
    print(stages[lives])

#########################################################################################################
