from unittest import TestCase, mock
from Project_Package.CardGame import CardGame

class TestCardGame(TestCase):
    def setUp(self):
        self.test_game = CardGame('sagi', 'adi')
        print('setUP')

    def tearDown(self):
        print('tearDown')

    def test_new_game(self):
        self.test_game.new_game()
        self.test_game.new_game()
        self.assertEqual(self.test_game.new_game ,1)

    def test_get_winner(self):
        self.test_game.player1.cardList = []  # checking if player 1 does win if his list is shorter
        self.test_game.player2.cardList = [1, 2, 3, 4, 5, 6]
        self.assertEqual(self.test_game.get_winner(), self.test_game.player1)
        print("The method returns the expected value")
