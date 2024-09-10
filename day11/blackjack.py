import  random
header= """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      '------'                           |__/
      """
print(header)

all_cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
player_cards = []
dealer_cards = []

def calculate_cards_value(cards):
    cards_sum = 0
    for card in cards:
        if card == 'J'or card =='Q' or card == 'K':
            cards_sum += 10
        elif card == 'A':
            cards_sum += 11
        else:
            cards_sum += int(card)
    if cards_sum > 21 and 'A' in cards:
        cards_sum -= 10
    return cards_sum


while True:
    play_game = input("Would you like to play game of blackjack ? 'y' or 'n': ")
    if play_game.lower() == "n":
        break
    elif play_game.lower() == "y":
        player_cards = []
        dealer_cards = []
        player_cards.append(random.choice(all_cards))
        player_cards.append(random.choice(all_cards))
        print(player_cards)
        dealer_cards.append(random.choice(all_cards))
        print(dealer_cards)
        player_sum = calculate_cards_value(player_cards,)
        if player_sum < 21:
            while player_sum < 21:
                additional_card = input("Would you like one more card? 'y' or 'n': ")
                if additional_card.lower() == "y":
                    print("Adding one card")
                    player_cards.append(random.choice(all_cards))
                    player_sum = calculate_cards_value(player_cards)
                    print(player_cards)
                else:
                    print("Dealer flips the card")
                    dealer_cards.append(random.choice(all_cards))
                    dealer_sum = calculate_cards_value(dealer_cards)
                    print(dealer_cards)
                    while dealer_sum < 17:
                        print("Dealer draws a card")
                        dealer_cards.append(random.choice(all_cards))
                        dealer_sum = calculate_cards_value(dealer_cards)
                        print(dealer_cards)
                    if dealer_sum < player_sum and dealer_sum < 22:
                        print("YOU WIN")
                        break
                    elif player_sum < dealer_sum < 22:
                        print("DEALER WINS")
                        break
                    else:
                        print("PUSH")
                        break
                print("BUST")
    else:
        print("Please select 'y' for yes and 'n' for no!")
