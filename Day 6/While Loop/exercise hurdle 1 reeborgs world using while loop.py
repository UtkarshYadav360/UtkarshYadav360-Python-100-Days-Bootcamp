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

# total number of hurdles   
total_hurdles = 6

# loop will run until total_hurdles becomes greater than 0
while total_hurdles > 0 :
    # player will jump until the above condition becomes false
    jump()
    # subtracting 1 from the total_hurdles when the loop runs each time
    total_hurdles-=1

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
