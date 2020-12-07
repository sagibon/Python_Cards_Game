from unittest import TestCase
from Project_Package.DeckOfCards import DeckOfCards
from Project_Package.Player import Player
from Project_Package.Card import Card

class TestPlayer(TestCase):
    def setUp(self):
        print("setUp")
        self.deck_test = DeckOfCards()
        self.player1 = Player('sagi', 10)
        self.player1.set_hand(self.player1.NumOfCards)

    def tearDown(self):
        print("tearDown")


    def test_get_card(self):
        # checks if the get_card function return 'Card' type object
        self.assertTrue(type(self.player1.get_card()) is Card)


    def test_show(self):
        self.player1.show()
