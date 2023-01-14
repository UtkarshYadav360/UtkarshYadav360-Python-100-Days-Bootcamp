# THIS CODE WORKS IN REEBORGS WORLD GAME.

# INTERMEDIATE PROBLEM DON'T BE UPSET IF CAN'T UNDERSTANDABLE!

# making a function to turn around
def turn_around() :
    turn_left()
    turn_left()

# making a function to turn right
def turn_right() :
    turn_around()
    turn_left()
    
# making a function that jumps the player over the hurdles
def jump() :
    turn_left()
    while wall_on_right() :
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear() :
        move()
    turn_left()
    
# the different functions used below are the already given functions.

# this loop will run if the front is clear
while front_is_clear() :
    move()
    # player will turn left after the above loop is completed
turn_left()

# this loop will take player to the final destination
while not at_goal() :
    if right_is_clear() :
        turn_right()
        move()
    elif front_is_clear() :
        move()
    else :
        turn_left()
        