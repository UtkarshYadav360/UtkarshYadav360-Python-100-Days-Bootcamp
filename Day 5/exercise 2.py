# HIGH SCORE :

# PRINT THE MAXIMUM SCORE FROM THE STUDENT SCORES LIST GIVEN BY THE USER

# DO NOT USE max() FUNCTION , WHICH FINDS THE MAXIMUM NUMBER
# WHEREAS min() FUNCTION , FINDS THE MINIMUM NUMBER







# greeting to the user
print("Welcome To The Maximum Score Finder!")

# student scores input
student_scores = input("Enter a list of student score out of 100, comma seperated : ").split(",")

# changing user input into a list
for n in range(0,len(student_scores)) :
    student_scores[n] = int(student_scores[n])

# variable that stores the highest score from the user input
highest_score = 0

# iterating scores in student_score list
for scores in student_scores :
    # condition
    if scores > highest_score :
        highest_score = scores
# final output
print(f"The highest score is {highest_score}.")
