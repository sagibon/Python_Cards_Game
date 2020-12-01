from random import randint as random

from Project_Package.card import DeckOfCards, Card

d = DeckOfCards()  # creating an instance of DeckOfCards game to give the player cards from the deck

class Player:
   # לא יכול להיות גדול מ26, להוסיף אחרי זה
    def __init__(self, name, NumOfCards = 10):  #מאתחל את האובייקט ב10 קלפים בתור ברירת מחדל ובשם
        self.NumOfCards = NumOfCards
        self.cardList = []  # The list of card objects
        self.PlayerName = name

    def set_hand(self, num_of_cards):

        for i in range(num_of_cards):
            self.cardList += [d.deal_one()]  # Adds a random card number to the player deck card from deck Card local variable instance we created
        print(self.cardList)

    def get_card(self):
        return d.deal_one()  # Picking a random card from the deck and returning the value

    def add_card(self, *card):
        self.cardList += card

    def show(self):
        print(f"Player name: {self.PlayerName} \n{self.cardList}")




