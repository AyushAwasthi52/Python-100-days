import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(hand):
    score = sum(hand)
    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

player_cards = [deal_card(), deal_card()]
dealer_cards = [deal_card(), deal_card()]

print(f"Dealer's first card: {dealer_cards[0]}")
print(f"Your cards: {player_cards}, Score: {calculate_score(player_cards)}")

# Player turn
while True:
    if input("Type y to get another card, n to pass: ") != 'y':
        break
    
    player_cards.append(deal_card())
    score = calculate_score(player_cards)
    
    print(f"Your cards: {player_cards}, Score: {score}")
    
    if score > 21:
        print("You lose! Bust.")
        exit()

# Dealer turn
while calculate_score(dealer_cards) < 17:
    dealer_cards.append(deal_card())

print(f"Dealer cards: {dealer_cards}, Score: {calculate_score(dealer_cards)}")

# Final result
player_score = calculate_score(player_cards)
dealer_score = calculate_score(dealer_cards)

if dealer_score > 21 or player_score > dealer_score:
    print("You win!")
elif player_score == dealer_score:
    print("Draw!")
else:
    print("You lose!")