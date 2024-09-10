_heading = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     '"=.|                  |
|___________________|__"=._o'"-._        '"=.______________|___________________
          |                '"=._o'"=._      _'"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
          |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
 _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
|                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
|___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************'''

print(_heading)
print("Welcome to the Treasure Island.\n Your mission is to find the treasure")
while True:
    print("You're at a cross road. Where do you want to go?")
    move_1 = input('\tType "left" or "right" \n').lower()
    if move_1 == "left":
        print("You've come to a lake. There is an island in the middle of the lake.")
        move_2 = input('\tType "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
        if move_2 == "wait":
            print("You arrive at the island unharmed. There is a house with 3 doors.")
            move_3 = input("One red, one yellow and one blue. Which colour do you choose? \n").lower()
            if move_3 == "red":
                print("It's a room full of fire. Game Over.")
                break
            elif move_3 == "yellow":
                print("You found the treasure! You Win!")
                break
            elif move_3 == "blue":
                print("You enter a room of beasts. Game Over.")
                break
            else:
                print("\n *** Please input correct data that is offered *** \n *** GAME RESTARTING *** \n")
                continue
        elif move_2 == "swim":
            print("You get attacked by an angry trout. Game Over.")
        else:
            print("\n *** Please input correct data that is offered *** \n *** GAME RESTARTING *** \n")
            continue

    elif move_1 == "right":
        print("You fell into a hole. Game Over.")
        break
    else:
        print("\n *** Please input correct data that is offered *** \n *** GAME RESTARTING ***\n")
        continue