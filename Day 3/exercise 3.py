# LEAP YEAR :

# TAKE USER INPUT FOR THE YEAR AND, CHECK WHETHER THE YEAR IS LEAP OR NOT

# if year is completely divisible by 4 
# except it is evenly divisible by 100 
# unless it is also completely divisible by 400


# EXAMPLE ==>
# 2000 / 4 = 500 [LEAP]
# 2000 / 100 = 20 [NOT LEAP]
# 2000 / 400 = 5 [LEAP]
# SO THE YEAR 2000 IS A LEAP YEAR






# greeting to the user
print("Leap Year Check")

# year input
year = int(input("Enter the year you want to check : "))

# conditions
if year % 4 == 0 :
    if year % 100 != 0 :
        print("It is a Leap Year.")
    else :
        if year % 400 == 0 :
            print("It is a Leap Year.")
        else :
            print("It is not a Leap Year.")
else :
    print("It is not a Leap Year.")
