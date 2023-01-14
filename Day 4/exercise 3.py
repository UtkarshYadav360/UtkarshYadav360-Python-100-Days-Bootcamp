# TREASURE MAP :




# greeting to the user
print("Choose A Place Where You Want To Hide The Treasure!")

# making three lists with empty spaces
row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]

# making a nested list
locator_map = [row1,row2,row3]


# position input where user want to hide the treasure
position = input("Where do you want to put the treasure? [Row Column] : ")

# accessing input from the user
row = int(position[0])
column = int(position[1])

locator_map[row-1][column-1] = "X"

# printing all three lists so it looks like map
print(f"{row1}\n{row2}\n{row3}")
