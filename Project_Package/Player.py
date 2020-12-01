from random import randint as random
from Project_Package.CardGame import CardGame
from Project_Package.card import DeckOfCards, Card

c = CardGame()  # creating an instance of cardgame class to take the card number for each player from there (second line down here as well)
d = DeckOfCards()  # creating an instance of DeckOfCards game to give the player cards from the deck

class Player:
    number_of_cards = c.NumOfCards  # לא יכול להיות גדול מ26, להוסיף אחרי זה
    def __init__(self, name, NumOfCards = 10):  #מאתחל את האובייקט ב10 קלפים בתור ברירת מחדל ובשם
        self.NumOfCards = NumOfCards
        self.cardList = []  # The list of card objects
        self.PlayerName = name

    def set_hand(self, deck_cards):

        for i in range(self.NumOfCards):
            self.cardList += [d.deal_one()]  # Adds a random card number to the player deck card from deck Card local variable instance we created
            #  self.cardList += [card_deck[random(1, len(deck_cards))]]
        print(self.cardList)

    def get_card(self):
        return d.deal_one()  # Picking a random card from the deck and returning the value

    def add_card(self, *card):
        self.cardList += card

    def show(self):
        print(f"Player name: {self.PlayerName} \n{self.cardList}")




