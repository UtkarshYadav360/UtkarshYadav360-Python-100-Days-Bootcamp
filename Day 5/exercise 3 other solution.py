# ADDING EVENS :

# PRINT THE SUM OF ALL THE EVEN NUMBERS FROM 1 TO 100



# variable that stores the sum of even numbers from 1 to 100 
i_sum = 0

# generating all numbers from 1 to 100
for i in range(1,101) :
    # condition
    if i % 2 == 0 : # the number will be even
        # adding even numbers to variable 'i_sum'
        i_sum+=i

# final output
print(f"The sum of all even numbers from 1 to 100 is {i_sum}.")
