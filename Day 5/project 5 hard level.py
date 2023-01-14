# PASSWORD GENERATOR :

# HARD LEVEL SOLUTION
# The password pattern will be random
# PASSWORD = w$1)sqt3! 

# random.shuffle() method is used to shuffle the items of a list randomly




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

# variable with empty list that stores the final generated password list
password_list = []

# getting count of letters that user want in their password
for letter in range(1,letters_input+1) :
    # generating random letters from the list of letters and adding it to the variable 'password'
    password_list+=random.choice(letters)

# getting the count of numbers that user want in their password
for number in range(1,numbers_input+1) :
    # generating random numbers from the list of numbers and adding it to the variable 'password'
    password_list+=random.choice(numbers)

# getting count of symbols that user want in their password
for symbol in range(1,symbols_input+1) :
    # generating random number from the list of numbers and adding it to the variable 'password'
    password_list+=random.choice(symbols)

# shuffling the 'password_list' to get a strong password
random.shuffle(password_list)


# variable that stores the final strong password generated
password = ""

# iterating items in the 'password_list'
for char in password_list :
    # adding iterated items to the variable 'password' so the final output will be a string not a list
    password+=char

# final password
print(f"This can be a strong password {password}")
