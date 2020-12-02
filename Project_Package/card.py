import random


class Card:
    def __init__(self, value, suit):  # 1 זה אס (הכי גבוה) ואז כרגיל 2-13 (11-נסיך, 12-מלכה, 13-מלך)
        self.value = value  # נותן ערך הקלף
        self.suit = suit  # נותן צורה לקלף

    def __repr__(self):
        suits_Translate = {1: "Diamond", 2: "Spade", 3: "Heart", 4: "Club"}
        value_Translate = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
        if self.value in value_Translate:
            return f" {value_Translate[self.value]} of {suits_Translate[self.suit]}"
        else:
            return f" {self.value} of {suits_Translate[self.suit]}"

    def who_higher(self, card2):  # הבדיקה של איזה קלף יותר חזק
        if self.value > card2.value:  # אם ערך קלף 1 יותר גבוה מערך קלף 2
            if card2.value == 1:  # בודק אם ערך קלף 2 הוא אס
                return card2  # אם כן מחזיר לי את הקלף השני
            return self  # אם קלף 2 לא אס, יחזיר לי את קלף 1
        elif self.value < card2.value:  # אותה בדיקה בדיוק רק בודק אם הקלף השני גבוה ממנו
            if self.value == 1:
                return self
            return card2
        else:
            if self.suit > card2.suit:
                return self
            elif self.suit < card2.suit:
                return card2
        return "tie"  # אם בסופו של דבר לא קרה כלום וזה הגיע לכאן, משמע הקלפים שווים


class DeckOfCards:
    def __init__(self):
        self.deck = []  # החפיסה עצמה עם כל הקלפים
        for i in range(4):
            for j in range(13):
                self.deck += [Card(j + 1, i + 1)]

    def shuffle(self):  # מתודה שמערבבת את החפיסה
        random.shuffle(self.deck)

    def deal_one(self, deck=0):  # מתודה שמוציאה קלף רנדומלי מהחפיסה ומחזירה אותו
        if type(deck) is list:
            self.deck = deck
        a = random.choice(self.deck)
        self.deck.remove(a)
        return a

    def show(self):  # מתודה שמדפיסה את החפיסה
        print(self.deck)
