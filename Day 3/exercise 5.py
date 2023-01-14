# LOVE CALCULATOR :

# .lower() method lowercase all the letters of a string
# .count() method count a specific string in a given string




#greeting to the user
print("Welcome To The Love Calculator!")

# both names input
name1 = input("Enter your name : ")
name2 = input("Enter their name : ")

# lowered and combined names
both_names = name1+name2.lower()

# checking name in true
t = both_names.count("t")
r = both_names.count("r")
u = both_names.count("u")
e = both_names.count("e")

# first value of love score
true = t+r+u+e

# checking name in love
l = both_names.count("l")
o = both_names.count("o")
v = both_names.count("v")
e = both_names.count("e")

# last value of love score
love = l+o+v+e

# love score
love_score = str(true)+str(love)

# love score into integer
love_score = int(love_score)

# conditions for the interpretations for both names
if (love_score < 10) or (love_score > 90) :
    print(f"Your Love Score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50) :
    print(f"Your Love Score is {love_score}, you are alright together.")
else :
    print(f"Your Love Score is {love_score}.")
