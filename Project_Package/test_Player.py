from unittest import TestCase
from Project_Package.Player import Player
from Project_Package.Card import Card


class TestPlayer(TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_get_card(self):
        self.player1 = Player('sagi', 2)
        self.player1.set_hand(self.player1.NumOfCards)
        # checks if the get_card function return 'Card' type object
        self.assertTrue(type(self.player1.get_card()) is Card)
        print("the type get_card gets is indeed card")

    def test_show(self):
        self.player2 = Player('adi', 2)
        self.player2.set_hand(self.player2.NumOfCards)
        self.player2.show()
