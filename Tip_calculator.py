print("Welcome to Tip calculator!")
bill  = float(input("What is the total amount of bill? "))
tip = int(input("How much tip would you like to give? 10, 12, 15? "))
people = int(input("How many people are contribute in this bill? "))
tip_as_percentage = tip/100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person have to pay {final_amount}")