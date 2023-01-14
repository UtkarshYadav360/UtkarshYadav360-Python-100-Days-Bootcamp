# THIS CODE WORKS IN REEBORGS WORLD GAME.
# making a function to turn around
def turn_around() :
    turn_left()
    turn_left()

# making a function to turn right
def turn_right() :
    turn_around()
    turn_left()
    
# making a function to move into a square
def turn_square() :
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()
    
turn_square()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
