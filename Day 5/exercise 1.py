# AVERAGE HEIGHT :

# PRINT AVERAGE HEIGHT FROM THE LIST OF STUDENT HEIGHTS(CM).
# sum() function gives the total sum of numbers.

# DO NOT USE len() AND sum() FUNCTION!




# greeting to the user
print("Welcome To The Average Height Calculator!")

# student heights input
student_heights = input("Enter a list of student heights(cm), comma seperated : ").split(",")

# changing user input into a list
for n in range(0, len(student_heights)) :
    # changing student heights into integer and changing it to a list
    student_heights[n] = int(student_heights[n])

# variable that stores the total sum of the student heights
total_height = 0

# adding total heights given by the user
for height in student_heights :
    # getting total sum of the heights by adding height to the variable 'total_height'
    total_height+=height

# variable that stores the total number of students given by user
number_of_students = 0

# getting total number of students
for students in student_heights :
    # adding 1 for each from student_heights student in number_of_students
    number_of_students+=1

# calculating average height from the student_heights
average_height = round(total_height/number_of_students)

# final output
print(f"The average height from the given student heights is {average_height}.")
