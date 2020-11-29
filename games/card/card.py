import random


class Card:
    def __init__(self, value, suit):  # 1 זה אס (הכי גבוה) ואז כרגיל 2-13 (11-נסיך, 12-מלכה, 13-מלך)
        self.value = value  # נותן ערך הקלף
        self.suit = suit  # נותן צורה לקלף

    def __repr__(self):
        return f"value: {self.value}, suit: {self.suit}"

    def who_higher(self, card2):  # הבדיקה של איזה קלף יותר חזק
        """אני רוצה לעשות כאן השוואה יותר חכמה, אבל עדיין לא יודע אם זה באמת יותר חכם. צריך לבדוק את העניין. (עם ___eq___ וזה)"""
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
                return card2
            elif self.suit < card2.suit:
                return self
        return "tie"  # אם בסופו של דבר לא קרה כלום וזה הגיע לכאן, משמע הקלפים שווים


class DeckOfCards:
    def __init__(self):
        self.deck = []  # החפיסה עצמה עם כל הקלפים
        for i in range(4):
            for j in range(13):
                self.deck += [Card(j + 1, i + 1)]

    def shuffle(self):  # מתודה שמערבבת את החפיסה
        random.shuffle(self.deck)

    def deal_one(self):  # מתודה שמוציאה קלף רנדומלי מהחפיסה ומחזירה אותו פנימה
        return random.choice(self.deck)

    def show(self):  # מתודה שמדפיסה את החפיסה
        print(self.deck)
