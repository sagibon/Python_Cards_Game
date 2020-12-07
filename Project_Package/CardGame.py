from Project_Package.DeckOfCards import DeckOfCards
from Project_Package.Player import Player
DeckClass = DeckOfCards()


class CardGame:

    def __init__(self, name1, name2, numOfCards=10):
        self.flag = 0  # flag to check if I can call the new_game method
        self.numOfCards = numOfCards
        self.player1 = Player(name1, numOfCards)  # initialising player objects for a new game
        self.player2 = Player(name2, numOfCards)  # initialising player objects for a new game
        self.cardDeck = DeckClass.deck  # Initializing a deck card for both players, that why we multiply by 2

    def new_game(self):
        if self.flag != 0:
            return "Error, cannot start a new game while you are already in a game."
        self.flag += 1  # Method callable once, Raise a flag and return it to check later if the method has been called
        self.player1.set_hand(self.numOfCards)   # Player 1 deck initialize through player class
        self.player2.set_hand(self.numOfCards)   # Player 2 deck initialize through player class
        return self.flag

    def get_winner(self):  # whoever has the less card amount will win
        # if player 1 has less cards returns him as the winner
        if len(self.player1.cardList) < len(self.player2.cardList):
            return self.player1
        # if player 1 has less cards returns him as the winner
        elif len(self.player1.cardList) > len(self.player2.cardList):
            return self.player2

        else:  # if they have an equal amount of cards returns None
            return None



