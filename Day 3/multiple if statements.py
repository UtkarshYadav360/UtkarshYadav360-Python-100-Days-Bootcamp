# MULTIPLE IF STATEMENTS :

# if condition1 :
#   do A
# if condition2 :
#   do B
# if condition3 :
#   do C




# greeting to the user
print("Welcome To The Roller Coster")

# height input
height = int(input("Enter your height : "))

# conditions
if height >= 120 :
    print("You can ride the roller coster.")
    age = int(input("Enter your age : "))
    if age < 12 :
        ticket_price = 5
    elif age <= 18 :
        ticket_price = 7
    else :
        ticket_price = 12
    photos = input("Do you want photos? [y/n] : ")
    if photos == "y" :
        print(f"Your total bill is ${ticket_price + 3}.")
    elif photos == "n" :
        print(f"Your ticket price is ${ticket_price}.")
    else :
        print("You entered something wrong!")
else :
    print("You need to grow taller to ride the roller coster.")

