from random import randint as random
from Project_Package.CardGame import CardGame as c

class Player:
    def __init__(self, name, NumOfCards = 10):  #מאתחל את האובייקט ב10 קלפים בתור ברירת מחדל ובשם
        self.NumOfCards = NumOfCards  # לא יכול להיות גדול מ26, להוסיף אחרי זה
        self.cardList = []  # The list of card objects
        self.PlayerName = name

    def set_hand(self):
        for i in range(self.NumOfCards):
            self.cardList += [random(1, 13)]  # Adds a random card number to the player deck card, Value 1 to 13 both included
        print(self.cardList)

    def get_card(self):
        return self.cardList.pop(random(1, len(self.cardList)))  # Removing a random card from the deck and returning the value

    def add_card(self, *card):
        self.cardList += card

    def show(self):
        print(f"Player name: {self.PlayerName} \n{self.cardList}")




