from random import randint as random
from Project_Package.CardGame import CardGame
from Project_Package.card import DeckOfCards

c = CardGame()  # creating an instance of cardgame class to take the card number for each player from there (second line down here as well)


class Player:
    number_of_cards = c.NumOfCards  # לא יכול להיות גדול מ26, להוסיף אחרי זה
    def __init__(self, name, number_of_cards):  #מאתחל את האובייקט ב10 קלפים בתור ברירת מחדל ובשם
        self.NumOfCards = number_of_cards
        self.cardList = []  # The list of card objects
        self.PlayerName = name

    def set_hand(self, deck_cards):
        d = DeckOfCards()  # creating an instance of DeckOfCards game to give the player cards from the deck
        card_deck = d.deck # Adding the card deck from DeckOfCards class to a local variable to use and give cards to the player
        for i in range(self.NumOfCards):
            self.cardList += [card_deck[random(1, len(deck_cards))]]  # Adds a random card number to the player deck card from deck Card local variable instance we created
        print(self.cardList)

    def get_card(self):
        return self.cardList.pop(random(1, len(self.cardList)))  # Removing a random card from the deck and returning the value

    def add_card(self, *card):
        self.cardList += card

    def show(self):
        print(f"Player name: {self.PlayerName} \n{self.cardList}")




