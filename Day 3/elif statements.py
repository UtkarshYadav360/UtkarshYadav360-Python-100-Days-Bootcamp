# IF ELIF ELSE STATEMENMTS :
# if condition1 :
#   do this
# elif condition2 :
#   do this
# elif condition3 :
#   do this
# else :
#   do this



# greeting to the user
print("Welcome To The Roller Coster")

# height input
height = int(input("Enter your height : "))

# conditions
if height >= 120 :
    print("You can ride the roller coster.")
    age = int(input("Enter your age : "))
    if age < 12 :
        print("Your ticket price is $5.")
    elif age <= 18 :
        print("Your ticket price is $7.")
    else :
        print("Your ticket price is $12.")
else :
    print("You have to grow taller to ride the roller coster.")
