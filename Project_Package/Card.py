

class Card:
    def __init__(self, value, suit):  # 1 זה אס (הכי גבוה) ואז כרגיל 2-13 (11-נסיך, 12-מלכה, 13-מלך)
        self.value = value  # נותן ערך הקלף
        self.suit = suit  # נותן צורה לקלף
        self.suits_symbols = {1: "\u2666", 2: "\u2660", 3: "\u2665", 4: "\u2663"}
        # suits_translate = {1: "Diamond", 2: "Spade", 3: "Heart", 4: "Club"}

    def __repr__(self):
        # letters meaning: {A: "Ace", J: "Jack", Q: "Queen", K: "King"}
        # a dictionary of all the possible card values that will appear on the card
        self.value_translate = {1: "A", 11: "J", 12: "Q", 13: "K", 2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10}
        if self.value in self.value_translate:
            return f" {self.value_translate[self.value]} of {self.suits_symbols[self.suit]}"
        else:
            return f" {self.value} of {self.suits_symbols[self.suit]}"

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
