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

    ThrownCards += [Card1]  # collecting all the thrown away cards
    ThrownCards += [Card2]
    if Card1 > Card2:
        player1.add_card(Card1, Card2)

    elif Card1 < Card2:
        player2.add_card(Card1, Card2)

print(CardGame.get_winner())  # Return the details of the winner
