# making function with more than 1 inputs
def greet_with(name, location) :
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# calling the 'greet_with' function by giving name and location to it
greet_with("Utkarsh Yadav","Ghaziabad") # name = "Utkarsh Yadav" location = "Ghaziabad"

greet_with("Ghaziabad", "Utkarsh Yadav") # name = "Ghaziabad" location = "Utkarsh Yadav"
# THE ABOVE CODE SHOWS POSITIONAL ARGUMENTS, WE CAN CHANGE THE ORDER OF OUR INPUT, BUT OUR FIRST INPUT ASSIGNS TO THE FIRST VARIABLE AND SECOND INPUT WILL ASSIGN TO THE SECOND VARIABLE WE PASSED IN OUR FUNCTION.



# IN POSITIONAL ARGUMENTS WE CAN SIMPLY ASSIGN THE VALUE TO THAT VARIABLE NAME WE WANT AND THAT IS PASSED IN THE FUNCTION.
greet_with(location="Ghaziabad",name = "Utkarsh Yadav") # this is an example of keyword arguments
