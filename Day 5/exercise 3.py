# ADDING EVENS :

# PRINT THE SUM OF ALL THE EVEN NUMBERS FROM 1 TO 100



# variable that stores the sum of even numbers from 1 to 100 
i_sum = 0

# generating all even numbers from 1 to 100
for i in range(2,101,2) :
    # adding even numbers to variable 'i_sum'
    i_sum+=i

# final output
print(f"The sum of all even numbers from 1 to 100 is {i_sum}.")
