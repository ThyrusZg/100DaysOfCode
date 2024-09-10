print("Welcome to Python Pizza Delivery")
pizza_size = input("What size of pizza would you like? S, M or L: ").lower()
pepperoni = input("Would you like pepperoni on the pizza? Y or N: ").lower()
extra_cheese = input("Would you like extra cheese on the pizza? Y or N: ").lower()

total_bill = 0

if pizza_size == "s":
    total_bill += 15
elif pizza_size == "m":
    total_bill += 20
elif pizza_size == "L":
    total_bill +=25
else:
    print("Invalid input")

if pepperoni == "y":
    if pizza_size == "s":
        total_bill += 2
    else:
        total_bill += 3
if extra_cheese == "y":
    total_bill += 1

print(f"Total bill to pay is {total_bill}$")
