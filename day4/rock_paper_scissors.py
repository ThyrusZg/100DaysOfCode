import random

_rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''
_paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''
_scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

print("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors")
user_input = input("> ")
computer_selection = str(random.randint(0, 2))

if user_input == "0":
    print(_rock)
elif user_input == "1":
    print(_paper)
elif user_input == "2":
    print(_scissors)
else:
    print("INVALID USER INPUT")
1
print("\nCOMPUTER CHOOSE:\n")
if computer_selection == "0":
    print(_rock)
elif computer_selection == "1":
    print(_paper)
elif computer_selection == "2":
    print(_scissors)

if user_input == "0" and computer_selection == "0":
    print("DRAW")
elif user_input == "0" and computer_selection =="1":
    print("COMPUTER WINS")
elif user_input == "0" and computer_selection =="2":
    print("YOU WIN")
elif user_input == "1" and computer_selection == "0":
    print("YOU WIN")
elif user_input == "1" and computer_selection =="1":
    print("DRAW")
elif user_input == "1" and computer_selection =="2":
    print("COMPUTER WINS")
elif user_input == "2" and computer_selection == "0":
    print("COMPUTER WINS")
elif user_input == "2" and computer_selection =="1":
    print("YOU WIN")
elif user_input == "2" and computer_selection =="2":
    print("DRAW")