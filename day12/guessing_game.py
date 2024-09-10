import random

header = """
   _____                     _              _____                      
  / ____|                   (_)            / ____|                     
 | |  __ _   _  ___  ___ ___ _ _ __   __ _| |  __  __ _ _ __ ___   ___ 
 | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` | | |_ |/ _` | '_ ` _ \ / _ \\
 | |__| | |_| |  __/\__ \__ \ | | | | (_| | |__| | (_| | | | | | |  __/
  \_____|\__,_|\___||___/___/_|_| |_|\__, |\_____|\__,_|_| |_| |_|\___|
                                      __/ |                            
                                     |___/                             
"""
print(header)
number_of_tries = 0

def pick_random_number():
    return random.randint(1,100)

print("Welcome to guessing game!\nI am thinking of a number between 1 and 100, can you guess the number?")
x = pick_random_number()
print(f"Psst, number I'm thinking of is {x}")
game_mode = input("Select game mode, 'easy' or 'hard'? > ")
if game_mode.lower() == 'easy':
    number_of_tries = 10
else:
    number_of_tries = 5

while number_of_tries != 0:
    print(f"You have {number_of_tries} tries left!")
    user_guess = int(input("Enter number: "))
    if user_guess == x:
        print(f"***You got it, the answer is {user_guess}! ***")
        break
    elif user_guess > x:
        print("***You are TOO HIGH, go lower!******")
        number_of_tries -= 1
    else:
        print("***You are TOO LOW, go higher!***")
        number_of_tries -= 1