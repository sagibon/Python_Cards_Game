from Project_Package.Player import Player
from Project_Package.CardGame import CardGame

player1 = Player('SAGI')
player2 = Player('ADI')

player1.show()    # Show return the details of a player
player2.show()    # Show return the details of a player

ThrownCards = []
# The game will last for 10 rounds
points1 = 0
points2 = 0
for round in range(10):
    Card1 = player1.get_card()  # getting a random card from the player1 deck
    Card2 = player2.get_card()  # getting a random card from the player2 deck

    print(f"First player's card:{Card1}      Second player's card:{Card2}")
    if Card1 > Card2:
        player2.add_card(Card1, Card2)  # Player with the strongest cards wins, other player takes both they're cards from this round
        points1 += 1  # adding 1 point to track who wins
        print(player1)  # prints the winning player in this round

    elif Card1 < Card2:
        player1.add_card(Card1, Card2)  # Player with the strongest cards wins, other player takes both they're cards from this round
        points2 += 1  # adding 1 point to track who wins
        print(player2)  # prints the winning player in this round
print(CardGame.get_winner())  # Return the details of the winner
