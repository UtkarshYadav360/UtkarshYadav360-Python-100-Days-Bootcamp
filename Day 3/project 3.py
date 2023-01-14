# TREASURE ISLAND





# greeting to the user
print("Welcome To The Treasure Island! Your Mission Is To Find The Treasure.")

# printing the treasure chest ascii art
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************\n
''')

# conditions for the game

# direction choice [left or right]
direction = input("Do you want to go left or right? [l/r] : ")
if direction == "l" :
    print("Amazing! You are safe for now.\n")
    # choice [swim or wait]
    choice = input("Do you want to swim or wait? [s/w] : ")
    if choice == "w" :
        print("Hmm! You are patient enough to wait for a boat.\n")
        # door choice [red,blue,yellow]
        door = input("Which door you want to open? Red,Blue,Yellow [r/b/y] : ")
        if door == "y" :
            print("Congratulations! You find the treasure.")
        elif door == "r" :
            print("OOPS! You fell into the lava.")
        elif door == "b" :
            print("OOPS! You were sinked into the Deadly Sea.")
        else :
            print("SORRY! You typed something wrong.")
    elif choice == "s" :
        print("HEY FOOL! You wanted to swim in the Crocodile River.")
    else :
        print("SORRY! You typed something wrong.")
elif direction == "r" :
    print("OOPS! You were bitten by Poisionous Snakes.")
else :
    print("SORRY! You typed something wrong.")
