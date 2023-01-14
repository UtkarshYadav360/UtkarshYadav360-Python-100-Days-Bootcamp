# TAKE USER HEIGHT AND WEIGHT AS INPUT AND, PRINT THE BMI OF THE USER  :
# bmi = weight/(height)**2




# height and weight input
height = input("Enter your height : ")
weight = input("Enter your weight : ")

# height and weight into integer and float
float_height = float(height)
int_weight = int(weight)

# calculate bmi
bmi = int_weight/(float_height)**2

# final output
print("Your BMI is",bmi)
