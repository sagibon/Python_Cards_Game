from unittest import TestCase
from Project_Package.DeckOfCards import DeckOfCards
from Project_Package.Card import Card


class TestDeckOfCards(TestCase):

    def setUp(self):
        print("setUp")
        self.check = DeckOfCards()

    def tearDown(self):
        print("tearDown")

    def test_shuffle(self):
        self.assertNotEqual(self.check, self.check.shuffle())
        self.assertTrue(type(self.check) is DeckOfCards)
        with self.assertRaises(TypeError):
            self.check.shuffle("something")

    def test_deal_one(self):
        a = self.check.deal_one()
        self.assertNotIn(a, self.check.deck)
        b = self.check.deal_one("something")
        self.assertNotIn(b, self.check.deck)
        c = [Card(1, 1), Card(2, 1)]
        self.check.deal_one(c)

    def test_show(self):
        self.check.show()
