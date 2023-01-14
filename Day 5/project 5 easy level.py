# PASSWORD GENERATOR :

# EASY LEVEL SOLUTION
# The password pattern will be like this [letters numbers symbols]
# PASSWORD = wa51($ 




# letters
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# numbers
numbers = ["0","1","2","3","4","5","6","7","8","9"]

# symbols
symbols = ["!","#","$","%","&","(",")","*","+"]

# greeting to the user
print("Welcome To The Password Generator!")

# input for number of letters in password
letters_input = int(input("How many letters would you like in your password? "))

# input for number of numbers in password
numbers_input = int(input("How many numbers would you like in your password? "))

# input for number of symbols in password
symbols_input = int(input("How many symbols would you like in your password? "))

# importing random
import random

# variable with empty string that stores the final generated password 
password = ""

# getting count of letters that user want in their password
for letter in range(1,letters_input+1) :
    # generating random letters from the list of letters and adding it to the variable 'password'
    password+=random.choice(letters)

# getting the count of numbers that user want in their password
for number in range(1,numbers_input+1) :
    # generating random numbers from the list of numbers and adding it to the variable 'password'
    password+=random.choice(numbers)

# getting count of symbols that user want in their password
for symbol in range(1,symbols_input+1) :
    # generating random number from the list of numbers and adding it to the variable 'password'
    password+=random.choice(symbols)

# final password
print(f"You can use this as your password {password}")
