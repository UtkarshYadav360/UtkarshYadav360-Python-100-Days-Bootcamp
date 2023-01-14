# WHO WILL PAY THE BILL

# .split() method splits the string into seperate using the specific given character
# DO NOT USE .choice() method! because it picks a random item from a list/sequence





# greeting to the user
print("Let's Decide Who Will Pay The Bill!")

# names input for those who are 
names = input("Enter everybody's name who is willing to pay the bill, seperated by comma : ").split(",")

# importing random
import random

# finding total number of names given
len_of_names = len(names)

# generating a random index position from the names given
rand_name_index = random.randint(0,len_of_names-1)

# getting name of the person to pay the bill
bill_pay_person = names[rand_name_index]

# final output
print(f"{bill_pay_person} will pay the bill.")
