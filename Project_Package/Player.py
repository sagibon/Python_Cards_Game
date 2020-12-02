from Project_Package.card import DeckOfCards
d = DeckOfCards()  # creating an instance of DeckOfCards game to give the player cards from the deck


class Player:
    def __init__(self, name, NumOfCards):  # cant have more than 26 cards each, need to add a condition
        self.NumOfCards = NumOfCards
        self.cardList = []  # The list of card objects
        self.PlayerName = name

    def __str__(self):
        return f"{self.PlayerName}"

    def set_hand(self, num_of_cards):
        for i in range(num_of_cards):
            self.cardList += [d.deal_one()]  # Adds a random card number to the player deck card from deck Card local variable instance we created

    def get_card(self):
        return d.deal_one(self.cardList)  # Picking a random card from the deck and returning the value

    def add_card(self, card1, card2):
        self.cardList += [card1]
        self.cardList += [card2]

    def show(self):
        print(f"Player name: {self.PlayerName} \n{self.cardList}")




