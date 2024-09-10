

header = """\
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

"""
print(header)
same_number = False
result = 0

def perform_calculation(number1, operation, number2):
    if operation == "+":
        return  number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    else:
        return number1 / number2

while True:
    if not same_number:
        user_number1 = float(input("What's the first number?"))
    else:
        user_number1 = result
    print("+\n-\n*\n/\nPick an operation:")
    user_operation = input(">:")
    user_number2 = float(input("What's the next number?"))
    result = perform_calculation(user_number1, user_operation, user_number2)
    print(str(user_number1) + " " + user_operation  + " " +  str(user_number2) + " = " + str(result))
    continuing = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation: ")
    if continuing == 'y':
        same_number = True
    else:
        same_number = False
