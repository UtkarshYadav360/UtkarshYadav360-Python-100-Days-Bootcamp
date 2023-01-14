# NESTED IF ELSE STATEMENT :

# if condition :
#   if another condiiton :
#       do this
#   else :
#       do this
# else :
#   do this




# greeting to the user
print("Welcome To The Roller Coster")

# height input
height = int(input("Enter your height : "))

# conditions
if height >= 120 :
    print("You can ride the roller coster.")
    # age input
    age = int(input("Enter your age : "))
    if age > 18 :
        print("Your ticket price is $12.")
    else :
        print("Your ticket price is $7.")
else :
    print("You cannot ride the roller coster.")
