# PIZZA ORDER :

# TAKE USER INPUT FOR THE PIZZA SIZE , TAKE USER INPUT FOR PEPPERONI , TAKE INPUT FOR EXTRA CHEESE AND, PRINT THE TOTAL BILL




# greeting to the user
print("Welcome To Python Pizza Deliveries!\n")

# pricings of the pizza
print("Menu and Pricings :")
print("Small Pizza = $15\nMedium Pizza = $20\nLarge Pizza = $25")
print("Pepperoni for small pizza = $2\nPepperoni for medium and large pizza = $3")
print("Extra Cheese for any size pizza = $1\n")

# pizza input
pizza_size = input("What size of pizza you want? [s,m,l] : ")
pepperoni = input("Do your want pepperoni? [y/n] : ")
extra_cheese = input("Do you want extra cheese? [y/n] : ")

# useful variables
bill = 0

# conditions
if pizza_size == "s" :
    bill+=15
elif pizza_size == "m" :
    bill+=20
elif pizza_size == "l" :
    bill+=25

if pepperoni == "y" :
    if pizza_size == "s" :
        bill+=2
    else :
        bill+=3

if extra_cheese == "y" :
    bill+=1
    
# final output
print(f"Your total bill is ${bill}.")
