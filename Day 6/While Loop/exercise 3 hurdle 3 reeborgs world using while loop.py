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
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# front_is_clear , wall_in_front and at_goal() are the already built functions.

# loop will run till the player is not at_goal() or at_goal() is False
while not at_goal() :
    # this condition will check if the above condition is True
    if front_is_clear() :
        # palyer will move if the both above conditions are True
        move()
    else :
        jump()
     