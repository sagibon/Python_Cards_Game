from Project_Package.Card import Card
import random


class DeckOfCards:
    def __init__(self):
        self.deck = []  # The main deck with all of the cards
        for i in range(4):
            for j in range(13):
                self.deck += [Card(j + 1, i + 1)]

    def shuffle(self):  # Method that shuffles the main deck
        random.shuffle(self.deck)

    def deal_one(self, deck=None):  # method that picks a random card from a deck of your choice (main one, players..)
        if type(deck) is list:  # validating that the deck is in fact a list type
            self.deck = deck
        a = random.choice(self.deck)  # picking random card
        self.deck.remove(a)  # removing card from the original deck
        return a

    def show(self, deck=None):  # prints the card deck

        if type(deck) is list:  # validating that the deck is in fact a list type
            self.deck = deck
        print(self.deck)
