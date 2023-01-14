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

# making player to jump over the total number of hurdles
for hurdle in range(1,total_hurdles+1) :
    jump()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
