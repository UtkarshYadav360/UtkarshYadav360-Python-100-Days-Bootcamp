# TIP CALCULATOR :

# TAKE TOTAL BILL AS INPUT , TAKE HOW MUCH PERCENT OF THE TIP WOULD LIKE TO GIVE FROM THE BILL AS INPUT , TAKE NUMBER OF PEOPLE TO SPLIT THE BILL AND, PRINT THE AMOUNT EACH PERSON SHOULD PAY
# PRINT OUTPUT SHOULD HAVE 2 DECIMAL VALUES






# total bill input
total_bill = float(input("Enter the total bill : "))

# tip input 
tip = input("What percent of the bill? You want to give the tip [10,12,15] : ")

# people to split the bill
people = int(input("How many peoples to split the bill? "))

# tip percentage
tip_percent = int(tip)/100

# tip amount
tip_amount = total_bill*tip_percent

# bill after tip
bill_after_tip = total_bill+tip_amount

# splitting the bill among the people
final_bill = bill_after_tip/people

# final output
print(f"Each person will pay {round(final_bill,2)} dollars.")
