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
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# at_goal() is an already built function that indicates the final destination of the player.
    
# loop will run till the at_goal() is not True.
while not at_goal() :
    # player will jump till the above condition becomes False
    jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
