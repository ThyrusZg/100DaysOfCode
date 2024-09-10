print("Welcome to the tip calculator !")
total_bill = float(input("What was the total bill? $ "))
tip = float(input("How much would you like to tip ? (%)"))
people = int(input("How many people will split the bill? "))
calculation = (total_bill+(total_bill * tip/100)) / people
print("Each person needs to pay " + str(calculation) + "$" )
