from Project_Package.DeckOfCards import DeckOfCards
d = DeckOfCards()  # creating an instance of DeckOfCards game to give the player cards from the deck


class Player:
    def __init__(self, name, numOfCards):  # cant have more than 26 cards each, need to add a condition
        if numOfCards > 26 or numOfCards < 1:  # checking number of cards, if not valid
            print("Cards should be between 1 and 26.")
            quit()  # stops the script.
        self.NumOfCards = numOfCards
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
        print(f"{self.PlayerName}'s cards: \n{self.cardList}")




