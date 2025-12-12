# TODO: TipCalculator
# 1. Print a welcome message
# 2. Ask for the total bill
# 3. Ask how much tip they would like to add
# 4. Ask how many people to split the bill
# 5. Calculate how much each person should pay

print("Welcome to the Tip Calculators!")
bills = float(input("What was the total bill? $"))
tips = int(input("how much tip would you like to tip? note 10%, 15%, 18% "))
num_of_guest = float(input("How many people to split the bill? "))

total_tip = bills * tips/100
TotalBill = ((bills + total_tip)/num_of_guest)
final_amount = round(TotalBill,2)

print(f"Each person should pay: ${final_amount}")


