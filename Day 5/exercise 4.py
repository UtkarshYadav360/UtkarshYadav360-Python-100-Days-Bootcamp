# FIZZ BUZZ :

# GENERATE NUMBERS FROM 1 TO 100 , IF THE NUMBER IS COMPLETELY DIVISIBLE BY 3 THEN PRINT 'FIZZ' , IF THE NUMBER IS COMPLETELY DIVISIBLE 5 PRINT 'BUZZ' , IF THE NUMBER IS COMPLETELY DIVISIBLE BY 3 AND 5 BOTH THEN PRINT FIZZBUZZ





# greeting to the user
print("Welcome To The FIZZBUZZ Game!")

# generating numbers from 1 to 100
for i in range(1,100) :
    # conditions
    # completely divisible by 3 and 5 both
    if i % 3 == 0 and i % 5 == 0 :
        print("FIZZBUZZ")
    # completely divisible by 3
    elif i % 3 == 0 :
        print("FIZZ")
    # completely divisible by 5
    elif i % 5 == 0 :
        print("BUZZ")
    # not completely divisible by (3 or 5) or (3 and 5)
    else :
        print(i)
