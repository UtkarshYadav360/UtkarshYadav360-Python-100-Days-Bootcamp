# BMI CALCULATOR 2.0 :

# CALCULATE THE BMI OF THE USER AND, PRINT THEIR BMI AND ALSO, PRINT THE INTERPRETATIONS FOR THE BMI




# height input
height = float(input("Enter your height in Meters: "))

# weight input
weight = float(input("Enter your weight in KG: "))

# calculating BMI
bmi = round((weight/(height)**2),2)

# conditions for interpretation about users BMI
if bmi < 18.5 :
    print(f"Your BMI is {bmi}.UNDERWEIGHT.")
elif bmi < 25 :
    print(f"Your BMI is {bmi}.NORMAL WEIGHT.")
elif bmi < 30 :
    print(f"Your BMI is {bmi}.OVERWEIGHT.")
elif bmi < 35 :
    print(f"Your BMI is {bmi}.OBESE.")
else :
    print(f"Your BMI is {bmi}.CLINICALLY OBESE.")
