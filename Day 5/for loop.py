# for loop SYNTAX :
# for item in list_of_items :
#   do something to each item


# accessing all list items using for loop
fruits = ["Apple","Peach","Pear"]
for fruit in fruits :
    print(fruit)

print()

# inside for loop and outside for loop
fruits = ["Apple","Peach","Pear"]
for fruit in fruits :
    print(fruit) # inside for loop
    print(fruit + " Pie") # inside for loop
print(fruit) # outside for loop
