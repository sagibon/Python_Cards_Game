from Project_Package.card import DeckOfCards
from Project_Package.Player import Player
DeckClass = DeckOfCards()


class CardGame:

    def __init__(self, name1, name2, NumOfCards = 10):
        self.flag = 0  # flag to check if I can call the new_game method
        self.NumOfCards = NumOfCards
        self.player1 = Player(name1)  # initialising player objects for a new game
        self.player2 = Player(name2)  # initialising player objects for a new game
        self.cardDeck = DeckClass.deck  # Initializing a deck card for both players, that why we multiply by 2

    def new_game(self):
        self.flag += 1  # Method callable once, I raise a flag and return it to check later if the method has been called
        if self.flag != 0:
            return "Error, cannot start a new game while you are already in a game."
        self.player1.set_hand(self.NumOfCards)   # Player 1 deck initialize through player class
        self.player2.set_hand(self.NumOfCards)   # Player 2 deck initialize through player class

        return self.flag

    def get_winner(self):  # whoever has the less card amount will win

        if len(self.player1list) < len(self.player2list):  # if player 1 has less cards returns him as the winner
            return self.player1

        elif len(self.player1list) > len(self.player2list):  # if player 1 has less cards returns him as the winner
            return self.player2

        else:  # if they have an equal amount of cards returns None
            return None



