# range() FUNCTION SYNTAX :
# for number in range(a,b) :
#   print(number)



# generating numbers from 1 to 10 using range() function
for number in range(1,11) : # 11 not included
    print(number)

print()

# step argument in range() function :
for number in range(1,11,2) : # step argument cannot be 1 because it makes no change
    print(number)

print()



# adding 1 to 100 numbes using range() function

# variable that stores the sum of 1 to 100
i_sum = 0

# generating 1 to 100 numbers
for i in range(1,101) :
    # adding numbers to variable i_sum
    i_sum+=i

# final output
print(i_sum)
