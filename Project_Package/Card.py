import random


class Card:
    def __init__(self, value, suit):  # 1 זה אס (הכי גבוה) ואז כרגיל 2-13 (11-נסיך, 12-מלכה, 13-מלך)
        self.value = value  # נותן ערך הקלף
        self.suit = suit  # נותן צורה לקלף

    def __repr__(self):
        suits_translate = {1: "Diamond", 2: "Spade", 3: "Heart", 4: "Club"}
        value_translate = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
        if self.value in value_translate:
            return f" {value_translate[self.value]} of {suits_translate[self.suit]}"
        else:
            return f" {self.value} of {suits_translate[self.suit]}"

    def who_higher(self, card2):  # Method to check which card is stronger

        if self.value > card2.value:  # If card 1 is higher than card 2
            if card2.value == 1:  # Checks if card 2 is an ace, an exception
                return card2  # and returns him as he is higher
            return self  # else returns the lower card

        elif self.value < card2.value:  # same condition as the previous, just opposite scenarios
            if self.value == 1:
                return self
            return card2

        else:
            if self.suit > card2.suit:
                return self
            elif self.suit < card2.suit:
                return card2
        return "tie"  # If the code gets until this point, its a tie (Equal cards)
