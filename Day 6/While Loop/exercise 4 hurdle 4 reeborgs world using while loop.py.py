# THIS CODE WORKS IN REEBORGS WORLD GAME.
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

while not at_goal() :
    if wall_in_front() :
        jump()
    else :
        move()
    
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
