from Project_Package.Player import Player
from Project_Package.CardGame import CardGame
from Project_Package.card import DeckOfCards, Card

DeckClass = DeckOfCards()
MainDeck = DeckClass.deck
player1 = Player('SAGI')
player2 = Player('ADI')
Game1 = CardGame(player1.PlayerName, player2.PlayerName, 5)

"""player1.set_hand(MainDeck)  # Giving random cards to each player from the deck
player2.set_hand(MainDeck)  # Giving random cards to each player from the deck"""
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
    Card1.who_higher(Card2) # need to add conditions to check whos card is higher and then take the cards and add to the other player


print(Game1.get_winner())  # Return the details of the winner
