# LIFE IN WEEKS :

# TAKE USER AGE AS INPUT AND PRINT THE NUMBER OF MONTHS,WEEKS AND DAYS LEFT IF THEY LIVE TILL 90
# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months





# user age input
age = input("Enter Your Age : ")

# age left of the user
age_left = 90 - int(age)

# months left
months = age_left*12

# weeks left
weeks = age_left*52

# days left
days = age_left*365

# final output
print(f"You have {months} months,{weeks} weeks and {days} days left if you live till 90.")
