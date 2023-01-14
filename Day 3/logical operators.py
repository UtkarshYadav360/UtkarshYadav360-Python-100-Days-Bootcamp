# LOGICAL OPERATORS :
# 1) and [returns True if both conditions are true]
# 2) or [returns True is any one or both of the conditions are true]
# 3) not [revrse the condition]


a = 35
b = 45
print(a % 5 == 0 and b % 5 == 0) # True
print(a % 5 == 5 and b % 5 == 0) # False

print(a % 7 == 0 or b % 23 == 0) # True
print(a % 5 == 1 or b % 7 == 9) # False

print(not a > 120) # True
print(not a < 120) # False

print()





# greeting to the user
print("Welcome To The Roller Coster")

# height input
height = int(input("Enter your height : "))

# conditions
if height >= 120 :
    print("You can ride the roller coster.")

    age = int(input("Enter your age : "))
    if age >= 45 and age <= 55 :
        ticket_price = 0
        print(f"Everything is going to be ok, have a free ride.")
    elif age < 12 :
        ticket_price = 5
        print(f"Child tickets are ${ticket_price}.")
    elif age <= 18 :
        ticket_price = 7
        print(f"Youth tickets are ${ticket_price}.")
    else :
        ticket_price = 12
        print(f"Adult tickets are ${ticket_price}.")

    photos = input("Do you want photos? [y/n] : ")
    if photos == "y" :
        print(f"Your total bill is ${ticket_price + 3}.")
else :
    print("You need to grow taller to ride the roller coster.")

