class CardGame:
    def __init__(self, NumOfCards = 10):
        self.flag = 0  # flag to check if I can call the new_game method
        self.NumOfCards = NumOfCards
        self.player1 = None
        self.player2 = None
        self.cardDeck = []
        for card in range(self.NumOfCards*2):  # Intializing a deck card for both players, that why we multiply by 2
            self.cardDeck += card  # 1 card deck object for this class,

    def new_game(self):
        self.flag += 1  # Method callable once, I raise a flag and return it to check later if the method has been called
        if self.flag != 0:
            return "Error, cannot start a new game while you are already in a game."
        self.player1list = []  # Player 1 deck
        self.player2list = []  # Player 1 deck
        for card in range(self.NumOfCards):
            self.player1list += self.cardDeck.pop(0, len(self.cardDeck))  #Intializing player 1's deck

        for card in range(self.NumOfCards):
            self.player2list += self.cardDeck.pop(0, len(self.cardDeck))  # Intializing player 1's deck

        return self.flag

    def get_winner(self):  # whoever has the less card amount will win
        if len(self.player1list) < len(self.player2list):  # if player 1 has less cards returns him as the winner
            return self.player1

        elif len(self.player1list) > len(self.player2list):  # if player 1 has less cards returns him as the winner
            return self.player2

        else:  # if they have an equal amount of cards returns None
            return None



